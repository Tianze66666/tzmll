from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import Comment
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin,UpdateModelMixin,CreateModelMixin,DestroyModelMixin
from .serilazers import CommentSerializer
from rest_framework.viewsets import ViewSetMixin


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