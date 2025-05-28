# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
from rest_framework import serializers
from goods.serializers import GoodsSerializer
from goods.models import Goods
from .models import Cart


class CartSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cart
		fields = '__all__'


class CartDetailSerializer(serializers.Serializer):
	sku_id = serializers.CharField(required=True)
	email = serializers.EmailField(required=True)
	nums = serializers.IntegerField()
	is_delete = serializers.BooleanField()
	goods = serializers.SerializerMethodField()

	def get_goods(self,obj):
		# ser = GoodsSerializer(Goods.objects.filter(sku_id=obj.sku_id).all(),many=True).data
		ser = GoodsSerializer(Goods.objects.filter(sku_id=obj.sku_id).first()).data
		return ser

	class Meta:
		model = Cart
		fields = '__all__'