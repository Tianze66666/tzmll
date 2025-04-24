# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from utils.password_encode import get_md5
from .models import User


class UserSerializer(serializers.ModelSerializer):
	#email作为用户名进行登录，需要进行唯一性验证
	password = serializers.CharField(write_only=True)
	birthday = serializers.DateTimeField(format="%Y-%m-%d")
	create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",required=False)
	email = serializers.EmailField(
		required=True,
		allow_blank=False,
		validators=[UniqueValidator(queryset=User.objects.all(), message='用户已经存在')]
	)

	def create(self, validated_data):
		validated_data['password'] = get_md5(validated_data['password'])
		result = User.objects.create(**validated_data)
		return result


	class Meta:
		model = User
		fields = "__all__"


