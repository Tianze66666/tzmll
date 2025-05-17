from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse
from django.views import View
from utils.ResponseMessage import MenuResponse
# noinspection PyUnresolvedReferences
from menu import models


# Create your views here.


class GoodsMainView(View):
	def get(self, request):
		main_menu = models.MainMenu.objects.all()
		result_list = [m for m in main_menu.values()]
		# for m in main_menu.values():
		# 	m.pop('id')
		# 	m.pop('main_menu_url')
		# 	result_list.append(m)
		return JsonResponse(MenuResponse.success(result_list))

	def post(self, request):
		return HttpResponse('ok')


class GoodsSubmenuView(View):
	def get(self,request):
		main_menu_id = request.GET.get('main_menu_id')
		sub_menu = models.SubMenu.objects.filter(main_menu_id=main_menu_id).all()
		result_list = []
		for m in sub_menu:
			result_list.append(m.__str__())
		message = MenuResponse.success(result_list)
		return JsonResponse(message)

	def post(self, request):
		return HttpResponse('ok')