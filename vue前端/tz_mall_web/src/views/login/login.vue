<template>
	<div class="login">
		<div class="title clearfix">
			<div class="logo fl">
				<Logo></Logo>
			</div>
				<div class="name fl">欢迎登录</div>
		</div>
		<div class="login-info">
			<div class="login-content">
				<div class="login-text">
					<div class="title">
						<img src="@/assets/images/login/warning.png" alt="" />
						你妈的给我打钱
					</div>
					<div class="login-name">
						账户登录
					</div>
					<div class="login-username">
						<label for="email">
							<img src="@/assets/images/login/username.png" alt="" />
						</label>
						<input type="text" id="username" placeholder="邮箱" v-model="userInfo.email" />
					</div>
					<div class="login-password">
						<label for="password">
							<img src="@/assets/images/login/password.png" alt="" />
						</label>
						<input type="password" id="password" placeholder="密码" v-model="userInfo.password" />
					</div>
					<a href="#" class="forget-password">忘记密码</a>
					<button class="login-commit" @click="login">登录</button>
					<div class="register">
						<a href="/register">立即注册</a>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { reactive } from 'vue';
import Logo from '@/components/common/logo'
import {loginRequest} from '@/network/user'
import {useStore} from 'vuex';
import {useRouter} from 'vue-router'

	const router = useRouter()
	const store = useStore()
	
	let userInfo = reactive({
		email:"",
		password:""
	})
	
	const login = ()=>{
		loginRequest(userInfo).then(res=>{
			if (res.status === 4000){
				alert('登录成功')				
				// 本地存储token 并使用vuex提取
				window.localStorage.setItem('token',res.data.token)
				window.localStorage.setItem('userName',res.data.user_name)
				store.commit('setIsLogin',true)
				store.commit('setUsername',res.data.user_name)
				// 页面跳转 回到主页
				router.push('/')
			}else{
				alert('登录失败',res.data)
			}
		})
	}
</script>

<style lang="less" scoped>
	.login{
		.title{
			width: 1000px;
			height: 80px;
			margin: 0 auto;
			line-height: 80px;
			.logo{
				height: 40px;
			}
			.name{
				font-size: 30px;
				margin-left: 10px;
				margin-top: 30px;
			}
		}
		.login-info{
			background-color: #e93854;
			margin-top: 30px;
			.login-content{
				width: 990px;
				height: 475px;
				margin: 0 auto;
				background-image: url('@/assets/images/login/login-muxi.png');
				.login-text{
					width: 350px;
					height: 380px;
					background-color: #fff;
					float: right;
					margin-top: 20px;
					.title{
						color: #999;
						height: 40px;
						width: 350px;
						line-height: 40px;
						text-align: center;
						background-color: #fff8f0;
						img{
							width: 16px;
							height: 16px;
							
						}
					}
					.login-name{
						height: 40px;
						width: 350px;
						line-height: 40px;
						text-align: center;
						color: #e93854;
						font-size: 18px;
						font-weight: bold;
						border-bottom: 1px solid #f4f4f4;
					}
					.login-username,.login-password{
						border: 1px solid #dbdbdb;
						width: 310px;
						height: 40px;
						margin: 30px auto 0px;
						line-height: 40px;
						label{
							display: inline-block;
							height: 40px;
							width: 40px;
							text-align: center;
							line-height: 40px;
							border-right: 1px solid #dbdbdb;
							background-color: #f4f4f4;
							img{
								width: 20px;
								height: 20px;
								text-align: center;
								line-height: 20px;
							}
						}
						input{
							padding-left: 10px;
						}
					}
					.forget-password{
						display: block;
						font-size: 12px;
						color: #666;
						text-align: right;
						width: 310px;
						margin-top: 20px;
						&:hover{
							color: #e93854;
						}
					}
						
					.login-commit{
						width: 310px;
						height: 35px;
						background-color: #e93854;
						color: white;
						margin-top: 20px;
						font-size: 20px;
						margin-left: 20px;
					}
					.register{
						margin-top: 20px;
						background-color: #fcfcfc;
						height: 50px;
						width: 350px;
						line-height: 50px;
						text-align: right;
						a{
							color: #e93854 ;
							font-size: 18px;
							margin-right: 20px;
							text-decoration: none;
							background:linear-gradient( to right, #e93854) no-repeat right bottom;
							background-size: 0 2px; 
							transition: background-size 0.3s;
							&:hover{
								color: #d7334f;
								background-position-x:left;
								background-size: 100% 2px;
							}
						}
					}
				}


			}
			
		}
	}
	
</style>