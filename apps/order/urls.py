# -*- coding: UTF-8 -*-
# @Author  ：天泽1344

from django.urls import path
from .views import OrderGoodsGenericAPIView

urlpatterns = [
	path('goods/', OrderGoodsGenericAPIView.as_view()),
]