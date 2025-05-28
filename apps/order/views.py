from django.http import JsonResponse
from utils.ResponseMessage import OrderResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import OrderGoods,Order
from .serializers import OrderGoodsSerializer,OrderSerializer,OrderManyGoodsSerializer
import time
from cart.models import Cart
# Create your views here.


class OrderGoodsGenericAPIView(GenericAPIView):
	queryset = OrderGoods.objects
	serializer_class = OrderGoodsSerializer
	def post(self,request):
		# self.get_queryset()
		# self.get_serializer()
		ser = self.get_serializer(data=request.data)
		ser.is_valid(raise_exception=True)
		ser.save()
		return JsonResponse({})

	# def get(self, request):
	# 	data = self.get_serializer(instance=self.get_queryset(),many=True)
	# 	return JsonResponse(data.data,safe=False)
	def get(self,request, *args, **kwargs):
		if not request.user.get('status'):
			return JsonResponse(request.user,safe=False)
		trade_no = kwargs.get('trade_no')
		email = request.user.get('data').get('email')
		db_result = Order.objects.filter(
				email=email,
				is_delete=0,
				trade_no=trade_no
			).first()
		# 序列化数据
		order_ser = OrderManyGoodsSerializer(instance=db_result)
		return OrderResponse.success(order_ser.data)

class OrderGenericAPIView(GenericAPIView):
	queryset = Order.objects
	serializer_class = OrderSerializer

	def post(self,request):
		if not request.user.get('status'):
			return JsonResponse(request.user,safe=False)
		email = request.user.get('data').get('email')
		request_data = request.data

		#生成订单号
		trade_no = int(time.time()*1000)
		trade_data = request_data['trade']
		# 具体的商品，传过来是一个列表
		goods_data = request_data['goods']
		trade_data['trade_no'] = trade_no
		trade_data['email'] = email
		trade_data['pay_status'] = 0
		trade_data['is_delete'] = 0
		serializer = self.get_serializer(data=trade_data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		for data in goods_data:
			goods_order_data = {}
			goods_order_data['trade_no'] = trade_no
			goods_order_data['sku_id'] = data['sku_id']
			goods_order_data['goods_num'] = data.get('nums')
			if not goods_order_data['goods_num']:
				goods_order_data['goods_num'] = data.get('goods_num')
			OrderGoods.objects.create(**goods_order_data).save()
			#把商品从购物车删除
			Cart.objects.filter(sku_id=data['sku_id'],email=email).update(is_delete=True)
		return OrderResponse.success(serializer.data)


	def get(self,request):
		if not request.user.get('status'):
			return JsonResponse(request.user,safe=False)
		email = request.user.get('data').get('email')
		request_data = request.data
		pay_status = request.GET.get('pay_status')
		if pay_status == '-1':
			db_result = Order.objects.filter(
				email=email,
				is_delete=0,
			).all().order_by('-create_time')
		else:
			db_result = Order.objects.filter(
				email=email,
				is_delete=0,
				pay_status=pay_status
			).all().order_by('-create_time')
		# 序列化数据
		order_ser = OrderManyGoodsSerializer(instance=db_result,many=True)
		return OrderResponse.success(order_ser.data)


class OrderDetailGenericAPIView(GenericAPIView):
	queryset = Order.objects
	serializer_class = OrderSerializer

	def post(self,request):
		if not request.user.get('status'):
			return JsonResponse(request.user,safe=False)
		# email = request.user.get('data').get('email')
		request_data = request.data
		trade_no = request_data['trade_no']
		self.get_queryset().filter(trade_no=trade_no).update(**request_data)
		return OrderResponse.success('ok')