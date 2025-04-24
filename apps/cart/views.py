from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Cart
from goods.models import Goods
from .serializers import CartSerializer
from utils.ResponseMessage import CartsResponse
from django.db.models import F
# Create your views here.

class CartAPIView(APIView):

	# TODO:补充登录权限认证
	def post(self,request):
		request_data = request.data
		email = request_data.get('email')
		sku_id = request_data.get('sku_id')
		nums = request_data.get('nums')
		is_delete = request_data.get('is_delete')
		goods = Goods.objects.filter(sku_id=sku_id)
		if is_delete:
			Cart.objects.filter(sku_id=sku_id,
			                    email=email).update(is_delete=True)
			return CartsResponse.success('成功删除')
		if not goods.exists():
			return CartsResponse.filed('商品不存在')
		cart = Cart.objects.filter(email=email,
		                            sku_id=sku_id,
		                            is_delete=False)
		if cart.exists():
			#如果购物车存在，商品数量加一
			cart = cart.first()
			cart.nums = nums+cart.nums
			cart.save()
			return CartsResponse.success("添加数量成功")
		Cart.objects.create(
			email=email,
			sku_id=sku_id,
			nums=nums,
			is_delete=False,
		)
		return CartsResponse.success('添加购物车成功')




		# exist
		#判断商品是否存在，如果不存在就插入
		# data = Cart.objects.filter(
		# 	email=email,
		# 	sku_id=sku_id,
		# 	is_delete=False
		# )
		# if data.exists():
		# 	data.get()
		# try:
		# 	data = Cart.objects.get(
		# 		email=email,
		# 		sku_id=sku_id,
		# 		is_delete=False
		# 	)
		# 	data.nums = data.nums + nums
		# 	data.save()
		# except Cart.DoesNotExist:
		# 	Cart.objects.create(
		# 		email=email,
		# 		sku_id=sku_id,
		# 		nums=nums,
		# 		is_delete=False,
		# 	)
		# return JsonResponse({'message':'ok'})
		return CartsResponse.success('ok')

	def get(self,request):
		email = request.GET.get('email')
		cart_result = Cart.objects.filter(email=email, is_delete=False).all()
		cart_ser = CartSerializer(instance=cart_result,many=True)
		return CartsResponse.success(cart_ser.data)


