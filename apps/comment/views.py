from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from .models import Comment
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin,UpdateModelMixin,CreateModelMixin,DestroyModelMixin
from .serilazers import CommentSerializer
from rest_framework.viewsets import ViewSetMixin
from utils.ResponseMessage import CommentResponse

# Create your views here.

class CommentGenericAPIView(ViewSetMixin,
                            GenericAPIView,
                            RetrieveModelMixin,
                            ListModelMixin,
                            UpdateModelMixin,
                            CreateModelMixin,
                            DestroyModelMixin):
	queryset = Comment.objects
	serializer_class = CommentSerializer

	def single(self,request,pk):
		if not request.user.get('status'):
			return JsonResponse({'status':False})
		return self.retrieve(request,pk)

	def my_list(self,request):
		return self.list(request,)

	def edit(self,request,pk):
		return self.update(request,pk)

	def my_save(self,request):
		return self.create(request)

	def my_delete(self,request,pk):
		return self.destroy(request,pk)

class CommentAPIView(APIView):
	def get(self, request):
		sku_id = request.GET.get('sku_id')
		page = int(request.GET.get('page', 1))
		start = (page - 1)*15
		end = page*15
		db_result = Comment.objects.filter(sku_id=sku_id).all()[start:end]
		ser_data = CommentSerializer(instance=db_result,many=True)
		return CommentResponse.success(ser_data.data)

class CommentCountAPIView(APIView):
	def get(self, request):
		sku_id = request.GET.get('sku_id')
		db_result = Comment.objects.filter(sku_id=sku_id).count()
		return CommentResponse.success(db_result)