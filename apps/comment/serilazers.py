# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'