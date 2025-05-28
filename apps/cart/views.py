from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Cart
from goods.models import Goods
from .serializers import CartSerializer,CartDetailSerializer
from utils.ResponseMessage import CartsResponse
from django.db.models import Sum

# Create your views here.

class CartAPIView(APIView):

	# TODO:补充登录权限认证
	def post(self,request):
		if not request.user.get('status') :
			return CartsResponse.filed(request.user)
		request_data = request.data
		email = request.user.get('data').get('email')
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
		# return CartsResponse.success('ok')

	def get(self,request):
		if not request.user.get('status'):
			return JsonResponse(request.user,safe=False)
		email = request.GET.get('email')
		cart_result = Cart.objects.filter(email=email, is_delete=False).all()
		cart_ser = CartSerializer(instance=cart_result,many=True)
		return CartsResponse.success(cart_ser.data)

#序列化器达到多表关联查询的目的

class CartDetailAPIView(APIView):
	def post(self,request):
		if not request.user.get('status') :
			return CartsResponse.filed(request.user)
		email =request.user.get('data').get('email')
		filters = {
			'email':email,
			'is_delete':False,
		}
		shopping_cart = Cart.objects.filter(**filters).all()
		db_data = CartDetailSerializer(instance=shopping_cart,many=True).data
		return CartsResponse.success(db_data)

class UpdataCartAPIView(APIView):
	def post(self,request):
		# 从token中获取到email
		if not request.user.get('status') :
			return CartsResponse.filed(request.user)
		email =request.user.get('data').get('email')
		request_data = request.data
		Cart.objects.filter(
			email = email,
			sku_id = request_data['sku_id'],
			is_delete = False
		).update(nums=request_data['nums'])
		return CartsResponse.success('ok')

# 获取购物车商品数量的接口
class CartCountAPIView(APIView):
	def post(self,request):
		if not request.user.get('status') :
			return CartsResponse.filed(request.user)
		email =request.user.get('data').get('email')
		user_cart_count = Cart.objects.filter(
											email = email,
											is_delete = False
										).aggregate(Sum('nums'))
		if not user_cart_count:
			user_cart_count = 0
		return CartsResponse.success(user_cart_count)

class DeleteCartGoodsAPIView(APIView):
	def post(self,request):
		# 从token中获取到email
		if not request.user.get('status') :
			return CartsResponse.filed(request.user)
		email =request.user.get('data').get('email')
		request_data = request.data
		Cart.objects.filter(
			email = email,
			sku_id__in = request_data,
			is_delete = False
		).update(is_delete=True)
		return CartsResponse.success('ok')