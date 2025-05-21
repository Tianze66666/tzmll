import json

from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer
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
		user_data_serialize.is_valid(raise_exception=True)
		user_obj = user_data_serialize.save()
		#序列化回json数据
		user_data = UserSerializer(instance=user_obj)
		#序列化，将json返回前端
		# return JsonResponse(user_data.data)
		return UserResponse.success(user_data.data)

	def get(self, request):
		email = request.GET.get('email',None)
		try:
			user_obj = User.objects.get(email=email)
			user_data = UserSerializer(user_obj)
			return UserResponse.success(user_data.data)
		except Exception as e:
			return UserResponse.filed('用户信息获取失败')

class LoginAPIView(GenericAPIView):
	def post(self,request):
		request_data = request.data
		email = request_data.get('email')
		try:
			user_data = User.objects.get(email=email)
		except Exception as e:
			return UserResponse.other('用户名或密码错误')
		# user_ser = UserSerializer(instance=user_data,many=False)
		request_password = request_data.get('password')
		request_password = get_md5(request_password)
		if request_password != user_data.password:
			return UserResponse.other('用户名或密码错误')
		payload = {
			'email':request_data.get('email')
		}
		token = create_token(payload=payload)
		return_data = {
			'token':token,
			'user_name':user_data.name
		}
		return UserResponse.success(return_data)
