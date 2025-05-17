# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
from django.urls import path
from . import views

urlpatterns = [
	path('category/<int:category_id>/<int:page>/',views.GoodsCategoryAPIView.as_view()),
	path('detail/<str:sku_id>',views.GoodsDetailAPIView.as_view()),
	path('find/',views.GoodsFindAPIView.as_view()),
	path('search/<str:keyword>/<int:page>/<int:order_by>',views.GoodsSearchAPIView.as_view()),
]