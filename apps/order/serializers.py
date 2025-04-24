# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
from rest_framework import serializers

from .models import OrderGoods


class OrderGoodsSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderGoods
		fields = '__all__'
