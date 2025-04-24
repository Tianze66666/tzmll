from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
# Create your views here.
from Tzmall.settings import PAGE_NUM
from .models import Goods
from utils.ResponseMessage import GoodsResponse
from Tzmall.settings import IMAGE_URL
from .serializers import GoodsSerializer
# 获取商品分类的接口
# http://localhost:8000/goods/categpry/1/1


class GoodsCategoryAPIView(APIView):
	def get(self,request,category_id,page):
		current_page = (page-1)*PAGE_NUM
		end_page = page*PAGE_NUM
		category_data = Goods.objects.filter(
			type_id = category_id,
		).all()[current_page:end_page]
		result_list = []
		for goods in category_data.values():
			goods['image'] = IMAGE_URL+goods['image']
			goods.pop('id')
			result_list.append(goods)
		return JsonResponse(GoodsResponse.success(result_list))

class GoodsDetailAPIView(APIView):
	def get(self,request,sku_id):
		goods_data = Goods.objects.filter(sku_id=sku_id).first()
		#序列化参数时instance   反序列化参数时data
		result = GoodsSerializer(instance=goods_data)

		return JsonResponse(GoodsResponse.success(result.data))