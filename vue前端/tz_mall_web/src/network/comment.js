import {request} from './request_config.js'

export function getCommentCount(skuId){
	return request({
		url:'/comment/count?sku_id='+skuId
	})
}

export function getCommentData(skuId,page){
	return request({
		url:'/comment/detail?sku_id='+skuId+'&page='+page
	})
}