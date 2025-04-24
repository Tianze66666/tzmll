# -*- coding: UTF-8 -*-
# @Author  ：天泽1344

from django.urls import path
from . import views

urlpatterns = [
	path('mainmenu/',views.GoodsMainView.as_view()),
	path('submenu/',views.GoodsSubmenuView.as_view())
]