import {addCart} from '@/network/cart'
import store from '@/store';

export function addcartData(skuId,nums=1,isDelete=0){
	let requestData = {
		sku_id:skuId,
		nums:nums,
		is_delete:isDelete
	}
	addCart(requestData).then(res=>{
		if (res.status === 3000){
			alert(res.data)
		}else{
			alert(res.data.error)
		}
		store.dispatch('updataCart')
	})
	
}

