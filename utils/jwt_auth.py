# -*- coding: UTF-8 -*-
# @Author  ：天泽1344
import datetime
import jwt
from rest_framework.authentication import BaseAuthentication

from Tzmall.settings import SECRET_KEY



def create_token(payload,timeout = 15):
	payload['exp'] = datetime.datetime.utcnow()+datetime.timedelta(minutes=timeout)
	result = jwt.encode(payload=payload, key=SECRET_KEY, algorithm='HS256')
	return result

def get_payload(token):
	result = {'status':False,
	          "data":None,
	          "error":None}
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
		result['data'] = payload
		result['status'] = True
	except Exception as e:
		result['error'] = f'{e}'
	return result

class JwtHeaderAuthentication(BaseAuthentication):

	def authenticate(self, request):
		token = request.headers.get('Authorization')
		result_payload = get_payload(token)
		return (result_payload,token)