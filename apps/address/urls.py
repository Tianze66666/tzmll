# -*- coding: UTF-8 -*-
# @Author  ：天泽1344

from django.urls import path,re_path
from . import views
from Tzmall.converts import EmailConverter
from django.urls.converters import register_converter

register_converter(EmailConverter,'ema')
# (?P<email>.*)
urlpatterns = [
	# path('',views.AddressGenericAPIView.as_view()),
	path(r'getone/<ema:email>',views.AddressGenericAPIView.as_view()),
	path(r'', views.AddressGenericAPIView.as_view()),
	re_path('list/',views.AddressListGenericAPIView.as_view()),
	path('edit/',views.UserAddressDetailGenericAPIView.as_view()),
	path('delete/',views.DeleteAddressGenericAPIView.as_view())
]