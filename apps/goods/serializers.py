# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
from rest_framework import serializers
from Tzmall.settings import IMAGE_URL
from .models import Goods

class GoodsSerializer(serializers.ModelSerializer):
	image = serializers.SerializerMethodField()
	create_time = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
	def get_image(self,obj):
		new_image = IMAGE_URL+obj.image
		return new_image


	class Meta:
		model = Goods
		fields = '__all__'