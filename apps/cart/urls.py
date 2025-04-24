# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
from django.urls import path
from . import views

urlpatterns = [
	path('add/',views.CartAPIView.as_view())
]