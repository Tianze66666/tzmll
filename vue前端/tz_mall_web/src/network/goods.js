import {request} from './request_config.js'

export function getGoodsListData(keyword,page,order){
	return request({
		url:'goods/search/'+keyword+'/'+page+'/'+order
	})
}

export function getKeywordCountData(keyword){
	return request({
		url:'goods/count/'+keyword
	})
}

export function getDoodsDetail(skuId){
	return request({
		url:'goods/detail/'+skuId
	})
}

