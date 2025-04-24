# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
from email.headerregistry import Address
from .models import UserAddress
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):
	create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',required=False)

	class Meta:
		model = UserAddress
		fields = '__all__'