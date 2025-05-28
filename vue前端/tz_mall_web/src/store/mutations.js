const mutations = {
	setIsLogin(state,payload){
		state.user.isLogin = payload
	},
	setUsername(state,payload){
		state.user.userName = payload
	},
	updateCartCount(state,payload){
		state.cartCount = payload
	}
}

export default mutations;