# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
"""响应数据工具"""
from django.http.response import JsonResponse, HttpResponse


class MenuResponse:
	@staticmethod
	def success(data):
		"""成功请求"""
		return {'status':1000,'data':data}

	@staticmethod
	def filed(data):
		"""失败请求"""
		return {'status':1001,'data':data}

	@staticmethod
	def other(data):
		"""不确定请求"""
		return {'status':1002,'data':data}

#商品的响应，全部都是2开头
class GoodsResponse:
	@staticmethod
	def success(data):
		"""成功请求"""
		return {'status':2000,'data':data}

	@staticmethod
	def filed(data):
		"""失败请求"""
		return {'status':2001,'data':data}

	@staticmethod
	def other(data):
		"""不确定请求"""
		return {'status':2002,'data':data}

#购物车响应 3开头
class CartsResponse:
	@staticmethod
	def success(data):
		"""成功请求"""
		return JsonResponse({'status':3000,'data':data})

	@staticmethod
	def filed(data):
		"""失败请求"""
		return JsonResponse({'status':3001,'data':data})

	@staticmethod
	def other(data):
		"""不确定请求"""
		return JsonResponse({'status':3002,'data':data})

class UserResponse:
	@staticmethod
	def success(data):
		"""成功请求"""
		return JsonResponse({'status': 4000, 'data': data})

	@staticmethod
	def filed(data):
		"""失败请求"""
		return JsonResponse({'status': 4001, 'data': data})

	@staticmethod
	def other(data):
		"""不确定请求"""
		return JsonResponse({'status': 4002, 'data': data})

class CommentResponse:
	@staticmethod
	def success(data):
		"""成功请求"""
		return JsonResponse({'status': 5000, 'data': data})

	@staticmethod
	def filed(data):
		"""失败请求"""
		return JsonResponse({'status': 5001, 'data': data})

	@staticmethod
	def other(data):
		"""不确定请求"""
		return JsonResponse({'status': 5002, 'data': data})


class OrderResponse:
	@staticmethod
	def success(data):
		"""成功请求"""
		return JsonResponse({'status': 6000, 'data': data})

	@staticmethod
	def filed(data):
		"""失败请求"""
		return JsonResponse({'status': 6001, 'data': data})

	@staticmethod
	def other(data):
		"""不确定请求"""
		return JsonResponse({'status': 6002, 'data': data})

class AddressResponse:
	@staticmethod
	def success(data):
		"""成功请求"""
		return JsonResponse({'status': 7000, 'data': data})

	@staticmethod
	def filed(data):
		"""失败请求"""
		return JsonResponse({'status': 7001, 'data': data})

	@staticmethod
	def other(data):
		"""不确定请求"""
		return JsonResponse({'status': 7002, 'data': data})