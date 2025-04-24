# -*- coding: UTF-8 -*-
# @Author  ：天泽1344

from hashlib import md5

def get_md5(param):
	md5_fac = md5()
	md5_fac.update(param.encode('utf-8'))
	md5_fac.update('tz1344'.encode('utf-8'))
	return md5_fac.hexdigest()