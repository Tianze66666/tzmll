# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
from rest_framework import serializers
from goods.models import Goods
from address.models import UserAddress
from .models import OrderGoods, Order
from Tzmall.settings import IMAGE_URL


class OrderGoodsSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderGoods
		fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'


class OrderManyGoodsSerializer(serializers.ModelSerializer):
	trade_no = serializers.CharField()
	email = serializers.CharField()
	order_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
	address_id = serializers.IntegerField()
	pay_status = serializers.CharField()
	pay_time = serializers.DateTimeField()
	ali_trade_no = serializers.CharField()
	is_delete = serializers.BooleanField(default=False)
	order_info = serializers.SerializerMethodField()
	create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
	signer_name = serializers.SerializerMethodField()

	def get_order_info(self, obj):
		ser = OrderGoodsSerializer(OrderGoods.objects.filter(trade_no=obj.trade_no).all(), many=True).data
		for i in ser:
			sku_id = i.get('sku_id')
			goods_data = Goods.objects.filter(sku_id=sku_id).first()
			i['p_price'] = goods_data.p_price
			i['image'] = IMAGE_URL + '/' + goods_data.image
			i['name'] = goods_data.name
			i['shop_name'] = goods_data.shop_name
		return ser

	def get_signer_name(self, obj):
		if obj.address_id is None:
			return None
		return UserAddress.objects.filter(id=obj.address_id).first().signer_name

	class Meta:
		model = Order
		fields = '__all__'
