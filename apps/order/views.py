from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import OrderGoods
from .serializers import OrderGoodsSerializer
# Create your views here.


class OrderGoodsGenericAPIView(GenericAPIView):
	queryset = OrderGoods.objects
	serializer_class = OrderGoodsSerializer

	def post(self,request):
		# self.get_queryset()
		# self.get_serializer()
		ser = self.get_serializer(data=request.data)
		ser.is_valid(raise_exception=True)
		ser.save()
		return JsonResponse({})

	def get(self, request):
		data = self.get_serializer(instance=self.get_queryset(),many=True)
		return JsonResponse(data.data,safe=False)
