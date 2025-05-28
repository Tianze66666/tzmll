import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
const GoodsList = ()=>import('../views/GoodsList/GoodsList')
const Detail = ()=>import('../views/Goods/Detail')
const login = ()=>import('../views/login/login')
const cart = ()=>import('../views/cart/cart')
const order = ()=>import('../views/order/order')
const profile = ()=>import('../views/profile/profile')
const register = ()=>import('../views/register/register')
const orderpay = ()=>import('../views/order/orderPay')

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
	meta:{
		title:'首页'
	}
  },
  {
	  // 问号的意思是，这个参数，可以传也可以不传
    path: '/goods_list/:keyword/:page/:order?',
    name: 'GoodsList',
    component: GoodsList,
  	meta:{
  		title:'商品列表页'
  	}
  },
  {
    path: '/detail/:skuId',
    name: 'Detail',
    component: Detail,
  	meta:{
  		title:'商品详情页',
  	}
  },
  {
    path: '/login',
    name: 'login',
    component: login,
  	meta:{
  		title:'登录'
  	}
  },
  {
    path: '/cart/detail/',
    name: 'cart',
    component: cart,
  	meta:{
  		title:'购物车',
  		isAuthRequired:true
  	}
  },
  {
    path: '/order/:trade_no',
    name: 'order',
    component: order,
  	meta:{
  		title:'订单详情',
  		isAuthRequired:true
  	}
  },
  {
    path: '/profile',
    name: 'profile',
    component:profile,
  	meta:{
  		title:'个人中心',
  		isAuthRequired:true
  	}
  },
  {
    path: '/register',
    name: 'register',
    component:register,
  	meta:{
  		title:'注册',
  	}
  },
  {
    path: '/order/pay',
    name: 'orderpay',
    component:orderpay,
  	meta:{
  		title:'支付界面',
		isAuthRequired:true
  	}
  },
  
  
]

import store from '../store'

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(function(to,from){
	document.title = to.meta.title
	if(to.meta.isAuthRequired===true && store.state.user.isLogin==false){
		router.push('/login')
	}
})

export default router
