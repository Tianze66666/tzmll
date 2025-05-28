import { getCartCounts } from "@/network/cart";

const actions = {
	updataCart({commit,state}){
		getCartCounts().then(res=>{
			let count = 0
			if(res.data.nums__sum>0){
				count = res.data.nums__sum
			}
			window.localStorage.setItem('count',count)
			commit('updateCartCount',count)
		})
	}
}

export default actions
