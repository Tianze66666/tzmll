import {request} from './request_config.js'

export function addAddressData(data){
	return request({
		url:'address/',
		method:'post',
		data
	})
}

export function getAllAddressData(){
	return request({
		url:'address/',
		method:'get',
	})
}

export function editAddressData(data){
	return request({
		url:'address/edit/',
		method:'post',
		data
	})
}

export function deleteAddressData(data){
	return request({
		url:'address/delete/',
		method:'post',
		data
	})
}