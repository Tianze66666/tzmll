# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
from rest_framework import serializers

from .models import Cart


class CartSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cart
		fields = '__all__'