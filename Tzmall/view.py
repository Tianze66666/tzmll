# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
from django.http import HttpResponse

def handler404(request, exception):
    return HttpResponse('<div style="margin:50px auto;"><h1 style="font-size:50px">傻逼请好好输入</h1></div>')