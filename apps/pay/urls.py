# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
from django.urls import path
from .views import ToAliPayPageAPIView,AlipayAPIView

urlpatterns = [
	path('alipay', ToAliPayPageAPIView.as_view()),
	path('alipay/return', AlipayAPIView.as_view()),
]