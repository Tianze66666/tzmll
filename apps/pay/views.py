from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .alipay import AliPay
from order.models import Order
from datetime import datetime
# Create your views here.


class ToAliPayPageAPIView(APIView):
	def post(self,request):
		if not request.user.get('status'):
			return JsonResponse(request.user,safe=False)
		trade_no = request.data.get('tradeNo')
		total_amount = request.data.get('orderAmount')

		alipay = AliPay()
		url = alipay.direct_pay(
			out_trade_no=trade_no,
			subject="主题:"+ trade_no,
			total_amount=total_amount,
		)
		# print(url)
		re_url = alipay.gateway + "?{data}".format(data=url)
		return JsonResponse({"alipay": re_url})

class AlipayAPIView(APIView):
	def get(self,request):
		processed_dict = {}
		for k,v in request.GET.items():
			processed_dict[k] = v
		sign = processed_dict.pop('sign',None)
		alipay = AliPay()
		is_verify = alipay.verify(processed_dict,sign)
		print('开始验证')
		if is_verify:
			print('验证通过')
			trade_no = processed_dict.get('out_trade_no')
			ali_trade_no = processed_dict.get('trade_no')
			# 0 待支付 1待确认 2支付完成 3已完成
			pay_status = '2'
			Order.objects.filter(trade_no=trade_no).update(
				ali_trade_no=ali_trade_no,
				pay_status=pay_status,
				pay_time = datetime.now()
			)
		return redirect('http://120.26.129.134:9000/profile?activeIndex=3')

	def post(self,request):
		processed_dict = {}
		for k,v in request.POST.items():
			processed_dict[k] = v
		sign = processed_dict.pop('sign',None)
		alipay = AliPay()
		is_verify = alipay.verify(processed_dict,sign)
		if is_verify:
			trade_no = processed_dict.get('out_trade_no')
			ali_trade_no = processed_dict.get('trade_no')
			# 0 待支付 1待确认 2支付完成 3已完成
			pay_status = '2'
			Order.objects.filter(trade_no=trade_no).update(
				ali_trade_no=ali_trade_no,
				pay_status=pay_status,
				pay_time = datetime.now()
			)
		return redirect('http://127.0.0.1:9000/profile?activeIndex=3')