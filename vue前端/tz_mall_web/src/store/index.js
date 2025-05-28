import { createStore } from 'vuex'
import mutations from './mutations.js'
import actions from './actions'

const state = {
	user:{
		isLogin:window.localStorage.getItem('token')?true:false,
		userName:window.localStorage.getItem('userName') ? window.localStorage.getItem('userName') : ''
	},
	cartCount:window.localStorage.getItem('count') || 0
}


export default createStore({
  state,
  
  getters: {
	  
  },
  
  mutations,
  
  actions,
  
  modules: {
	  
  }
})
