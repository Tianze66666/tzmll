<template>
	<div class="wrapper">
		<div class="header" >
			<span v-if="store.state.user.isLogin==false">
				<a href="/login">你好,请登录</a>
				<a href="/register" class="reg" >免费注册</a> &nbsp;&nbsp;&nbsp;|
			</span>
			<span v-else>
				<a href="/profile">{{store.state.user.userName}},欢迎</a>
				<a href="#" class="" @click="loginOut">退出登录</a> &nbsp;&nbsp;&nbsp;|
			</span>
			<a href="/profile?activeIndex=3">我的订单</a>

		</div>
		
	</div>
</template>

<script setup>
import { useStore } from 'vuex';
import { reactive } from 'vue';
import { useRouter } from 'vue-router';

	const router = useRouter()
	const store = useStore()
	
	const loginOut = ()=>{
		window.localStorage.setItem('token','')
		store.commit('setIsLogin',false)
		router.push('/')
	}

	
</script>

<style lang="less" scoped>
	.wrapper{
		background-color: #e3e4e5;
		height: 30px;
	
	}
	.header{
		width: var(--content-width);
		margin: 0 auto;
		text-align: right;
		line-height: 30px;
		
	} 
	.header a{
		color:var(--font-gray);
		margin-left:10px;
	}
	.header a:hover{
		color:var(--font-red)
	}
	.header .reg{
		color:var(--font-red);
	}
</style>