# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
from django.urls import path
from . import views

urlpatterns = [
	path('register/',views.UserAPIView.as_view()),
	path('login/',views.LoginAPIView.as_view())
]