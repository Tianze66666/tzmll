import decimal
import json
from datetime import datetime
from django.http import request
from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse
# Create your views here.
from Tzmall.settings import PAGE_NUM
from .models import Goods
from utils.ResponseMessage import GoodsResponse
from Tzmall.settings import IMAGE_URL
from .serializers import GoodsSerializer
from django.db import connection
from django.conf import settings
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


class GoodsFindAPIView(APIView):
	def get(self,request):
		goods_data = Goods.objects.filter(find=1).all()
		result = GoodsSerializer(goods_data, many=True)
		return JsonResponse(GoodsResponse.success(result.data))


class GoodsSearchAPIView(APIView):
	def get(self,request,keyword,page,order_by):
		"""
			SELECT r.comment_count ,g.image,g.name , g.p_price,g.shop_name,g.sku_id  from goods g
			LEFT JOIN
			(SELECT count(c.sku_id) as comment_count,c.sku_id from comment c GROUP BY c.sku_id
			) r
			on g.sku_id = r.sku_id
			where g.name like "%手机%"
			order by r.comment_count DESC limit 15
		"""

		order_dict = {
			1:'r.comment_count',
			2:'g.p_price',
		}
		limit_page = (page-1)*15
		#执行原生sql
		sql = """
			SELECT r.comment_count,concat('{}',g.image) as image,g.name,g.p_price,g.shop_name,g.sku_id  from goods g
			LEFT JOIN
			(SELECT count(c.sku_id) as comment_count,c.sku_id from comment c GROUP BY c.sku_id
			) r
			on g.sku_id = r.sku_id
			where g.name like "%{}%"
			order by {} DESC limit {},15
		""".format(settings.IMAGE_URL,keyword,order_dict.get(order_by,1),limit_page)
		cursor = connection.cursor()
		cursor.execute(sql)
		res = self.dict_fetchall(cursor)
		final_list = []
		for i in res:
			res_json = json.dumps(i,cls=DecimalEncoder,ensure_ascii=False)
			final_list.append(res_json)
		return JsonResponse(GoodsResponse.success(final_list))


	def dict_fetchall(self,cursor):
		desc = cursor.description
		return [dict(zip([col[0] for col in desc],row)) for row in cursor.fetchall()]


class DecimalEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, decimal.Decimal):
			return float(o)
		elif isinstance(0,datetime):
			return o.strftime("%Y-%m-%d %H:%M:%S")


class GoodsSearchDataCountAPIView(APIView):
	def get(self,request,keyword):
		count = Goods.objects.filter(name__contains=keyword).count()
		return HttpResponse(count)