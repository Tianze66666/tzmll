# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
from django.urls import path,re_path
from . import views
urlpatterns = [
	path('',views.CommentGenericAPIView.as_view({
		'get':"my_list",
		'post':'my_save'
	})),
	re_path('(?P<pk>.*)/',views.CommentGenericAPIView.as_view({
		'get':"single",
		'post':'edit',
		'delete':'my_delete'
	}))
]