# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
from django.urls import path
from . import views

urlpatterns = [
	path('add/',views.CartAPIView.as_view()),
	path('detail/',views.CartDetailAPIView.as_view()),
	path('num/',views.UpdataCartAPIView.as_view()),
	path('counts/',views.CartCountAPIView.as_view()),
	path('delete/',views.DeleteCartGoodsAPIView.as_view()),
]