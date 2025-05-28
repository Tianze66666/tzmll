# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from utils.password_encode import get_md5
from .models import User
from django.core.cache import cache
from urllib import parse

class UserSerializer(serializers.ModelSerializer):
	#email作为用户名进行登录，需要进行唯一性验证
	password = serializers.CharField(write_only=True)
	birthday = serializers.DateTimeField(format="%Y-%m-%d",required=False)
	create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",required=False)
	email = serializers.EmailField(
		required=True,
		allow_blank=False,
		validators=[UniqueValidator(queryset=User.objects.all(), message='用户已经存在')]
	)
	check_code = serializers.CharField(write_only=True, required=True, max_length=6, min_length=6)

	def create(self, validated_data):
		validated_data.pop('check_code',None)
		validated_data['password'] = get_md5(validated_data['password'])
		result = User.objects.create(**validated_data)
		return result

	def validate(self, attrs):
		email = attrs['email']
		input_code = attrs['check_code']
		cache_code = cache.get(f'check:code:{parse.quote(email)}')
		if cache_code is None:
			raise serializers.ValidationError("验证码不存在或已过期")

		if input_code != cache_code:
			raise serializers.ValidationError("验证码错误")

		return attrs


	class Meta:
		model = User
		fields = "__all__"

class UserDetailSerializer(UserSerializer):
	birthday = serializers.DateTimeField(format="%Y-%m-%d")
	name = serializers.CharField()
	gender = serializers.BooleanField(default=True)

	class Meta:
		model = User
		fields = ['birthday','name','gender']


class ResetPasswordSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField(write_only=True)
	# check_code = serializers.CharField(write_only=True, max_length=6, min_length=6)

	def validate(self, attrs):
		email = attrs['email']
		input_code = attrs['check_code']
		# 取缓存验证码
		cache_key = f'check:code:{parse.quote(email)}'
		# cache_code = cache.get(cache_key)
		# if cache_code is None:
		# 	raise serializers.ValidationError({'check_code': '验证码已过期或不存在'})
		# if input_code != cache_code:
		# 	raise serializers.ValidationError({'check_code': '验证码错误'})
		return attrs

	def save(self, **kwargs):
		email = self.validated_data['email']
		password = self.validated_data['password']
		try:
			user = User.objects.get(email=email)
		except User.DoesNotExist:
			raise serializers.ValidationError({'email': '该邮箱未注册'})
		# 自定义加密方法也可以在这里替换
		user.password = get_md5(password)
		user.save()
		return user