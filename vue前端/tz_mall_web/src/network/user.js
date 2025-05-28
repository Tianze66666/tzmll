import {request} from './request_config.js'

export function loginRequest(data){
	return request({
		url:'user/login/',
		method:'post',
		data
	})
}

export function getUserDetailRequest(){
	return request({
		url:'user/login/',
		method:'get',
	})
}


export function updateUserInfo(data){
	return request({
		url:'user/login/',
		method:'put',
		data
	})
}

export function registerUser(data){
	return request({
		url:'user/register/',
		method:'post',
		data
	})
}

export function sendCheckCode(email){
	return request({
		url:'user/code/'+email,
		method:'get',
	})
}

export function changePassword(data){
	return request({
		url:'user/change/',
		method:'post',
		data
	})
}