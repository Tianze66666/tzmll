import {request} from './request_config.js'

export function getCartDetailData(){
	return request({
		url:'cart/detail/',
		method:'post',
	})
}

export function updateGoodsNumData(data){
	return request({
		url:'cart/num/',
		method:'post',
		data
	})
}


export function addCart(data){
	return request({
		url:'cart/add/',
		method:'post',
		data
	})
}

export function getCartCounts(){
	return request({
		url:'cart/counts/',
		method:'post',
	})
}

export function deleteCartGoods(data){
	return request({
		url:'cart/delete/',
		method:'post',
		data
	})
}

