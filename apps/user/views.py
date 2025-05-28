import json
from datetime import datetime

from django.shortcuts import render
from django.http.response import JsonResponse
from django.core.cache import cache
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
from django.core.mail import send_mail
from rest_framework import status
import urllib.parse
from rest_framework.views import APIView
import random
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer,UserDetailSerializer,ResetPasswordSerializer
from utils.ResponseMessage import UserResponse
from .models import User
from utils.password_encode import get_md5
from utils.jwt_auth import create_token
# Create your views here.


class UserAPIView(APIView):
	# def post(self, request):
	# 	#反序列化，将json变成一个对象
	# 	request.data['password'] = get_md5(request.data['password'])
	# 	user_data_serialize = UserSerializer(data=request.data)
	# 	# user_data_serialize.is_valid(raise_exception=True)
	# 	user_data_serialize.is_valid(raise_exception=True)
	# 	user_obj = User.objects.create(**user_data_serialize.data)
	# 	#序列化回json数据
	# 	user_data = UserSerializer(instance=user_obj)
	# 	#序列化，将json返回前端
	# 	return JsonResponse(user_data.data)
	#
	def post(self, request):
		"""注册接口"""
		#反序列化，将json变成一个对象
		user_data_serialize = UserSerializer(data=request.data)
		# user_data_serialize.is_valid(raise_exception=True)
		try:
			user_data_serialize.is_valid(raise_exception=True)
		except Exception as e:
			return UserResponse.filed(f'false{e}')
		user_obj = user_data_serialize.save()
		#序列化回json数据
		user_data = UserSerializer(instance=user_obj)
		#序列化，将json返回前端
		# return JsonResponse(user_data.data)
		return UserResponse.success(user_data.data)

	def get(self, request):
		# if not request.user.get('status'):
		# 	return UserResponse.filed(request.user)
		# email = request.user.get('data').get('email')
		# try:
		# 	user_obj = User.objects.get(email=email)
		# 	user_data = UserSerializer(user_obj)
		# 	return UserResponse.success(user_data.data)
		# except Exception as e:
		# 	return UserResponse.filed('用户信息获取失败')
		pass



class LoginAPIView(GenericAPIView):
	def post(self,request):
		request_data = request.data
		email = request_data.get('email')
		try:
			user = User.objects.get(email=email)
		except Exception as e:
			return UserResponse.other('用户名或密码错误')
		# user_ser = UserSerializer(instance=user_data,many=False)
		request_password = request_data.get('password')
		request_password = get_md5(request_password)
		if request_password != user.password:
			return UserResponse.other('用户名或密码错误')
		payload = {
			'email':request_data.get('email')
		}
		token = create_token(payload=payload)
		return_data = {
			'token':token,
			'user_name':user.name
		}
		return UserResponse.success(return_data)

	def get(self, request):
		if not request.user.get('status'):
			return UserResponse.filed(request.user)
		email = request.user.get('data').get('email')
		try:
			user_obj = User.objects.get(email=email)
			user_data = UserDetailSerializer(user_obj)
			return UserResponse.success(user_data.data)
		except Exception as e:
			return UserResponse.filed('用户信息获取失败')

	def put(self,request):
		if not request.user.get('status'):
			return UserResponse.filed(request.user)
		email = request.user.get('data').get('email')
		request_data = request.data
		request_data['birthday'] = request_data['birthday'][:10]
		try:
			User.objects.filter(email=email).update(**request_data)
		except Exception as e:
			return UserResponse.filed('修改失败')
		return UserResponse.success('ok')

# 获取验证码
class GetCheckCodeAPIView(APIView):
	# get请求获取验证码,路径带邮箱
	def get(self,request,email):
		code =''.join([str(random.randint(0,9)) for _ in range(6)])
		cache.set(f'check:code:{urllib.parse.quote(email)}',code,timeout=300)
		#发送验证码
		subject = "【Tzmall】邮箱验证码"
		message = f"您的验证码是：{code}，有效期5分钟，请尽快使用。"
		from_email = None  # 使用settings里DEFAULT_FROM_EMAIL
		recipient_list = [email]
		send_mail(subject, message, from_email, recipient_list)
		return JsonResponse(f'ok',safe=False)

class ForgetPasswordAPIView(APIView):
	#获取验证码

	def get(self,request,email):
		user = User.objects.filter(email=email).first()
		if not user:
			return UserResponse.filed('用户未注册')
		code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
		cache.set(f'check:code:{urllib.parse.quote(email)}', code, timeout=300)
		# 发送验证码
		subject = "【Tzmall】邮箱验证码"
		message = f"您的验证码是：{code}，有效期5分钟，请尽快使用。"
		from_email = None  # 使用settings里DEFAULT_FROM_EMAIL
		recipient_list = [email]
		send_mail(subject, message, from_email, recipient_list)
		return JsonResponse(f'ok{code}', safe=False)

	def post(self,request):
		ser = ResetPasswordSerializer(data = request.data)
		if ser.is_valid(raise_exception=True):
			ser.save()
			return JsonResponse('ok')
		return JsonResponse('error',status=status.HTTP_400_BAD_REQUEST,safe=False)


class ChangePasswordAPIView(APIView):
	def post(self,request):
		if not request.user.get('status'):
			return UserResponse.filed(request.user)
		email = request.user.get('data').get('email')
		request_data = request.data
		old_password = request_data.get('old_password')
		new_password = request_data.get('new_password')
		old_password = get_md5(old_password)
		new_password = get_md5(new_password)
		user = User.objects.filter(email=email).first()
		if user.password != old_password:
			return UserResponse.filed('旧密码错误')
		user.password = new_password
		user.save()
		return UserResponse.success('ok')