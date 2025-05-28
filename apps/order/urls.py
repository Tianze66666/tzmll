# -*- coding: UTF-8 -*-
# @Author  ：天泽1344

from django.urls import path
from .views import OrderGoodsGenericAPIView,OrderGenericAPIView,OrderDetailGenericAPIView

urlpatterns = [
	path('',OrderGenericAPIView.as_view()),
	path('goods/<str:trade_no>/', OrderGoodsGenericAPIView.as_view()),
	path('update/',OrderDetailGenericAPIView.as_view())
]