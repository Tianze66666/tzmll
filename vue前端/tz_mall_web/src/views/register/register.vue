<template>
	<div class='register'>
		<div class="logo">
			<div>
				<logo></logo>
			</div>
			<span>欢迎注册</span>
		</div>
		<div class="main">
			<form class="info-form">
				<div class="username wrapper">
					<label for="username wrapper">用户名:</label>
					<input type="text" id="username" name="username" v-model="username">
				</div>
				<div class="password wrapper">
					<label for="password">密码:</label>
					<input type="password" id="password" name="username" v-model="password">
				</div>
				<div class="check-password wrapper">
					<label for="check-password">请确认密码:</label>
					<input type="password" id="check-password" name="username" v-model='checkPasswod'>
				</div>
				<div class="email wrapper">
					<label for="email">邮箱:</label>
					<input type="email" id="eamil" name="username" v-model="email">
				</div>
				<div class="check-code wrapper">
					<label for="email">验证码:</label>
					<input type="email" id="eamil" name="username" v-model='checkCode'>
					<button type="button" @click="getCheckCode">发送验证码</button>
				</div>
				<button type="button" @click="submit">注册</button>
			</form>
		</div>

	</div>

	
</template>

<script setup>
import logo from '@/components/common/logo'
import {ref} from 'vue'
import {registerUser,sendCheckCode} from '@/network/user'
import {useRouter} from 'vue-router'
	let username = ref('')
	let password = ref('')
	let checkPasswod = ref('')
	let email = ref('')
	let checkCode = ref('')
	const router = useRouter()
	
	const getCheckCode = ()=>{
		sendCheckCode(email.value).then(res=>{
			console.log(res);
		})
	}
	
	const submit = ()=>{
		let data = {
			name:username.value,
			password:password.value,
			email:email.value,
			check_code:checkCode.value,
		}
		registerUser(data).then(res=>{
			console.log(res);
			if(res.status===4000){
				alert('注册成功')
				router.push('/login')
			}else{
				alert('注册失败')
			}
		})
	
	}
	
</script>

<style scoped lang="less">
	.register{
		.logo{
			width: 500px;
			margin: 0 auto;
			display: flex;
			justify-content: center;
			span{
				margin-top:35px ;
				font-size: 50px;
			}
		}
		.main{
			width: 500px;
			margin: 0 auto;
			padding-top: 50px;
			.info-form{
				width: 500px;
				height: 450px;
				margin: 50 auto;
				border-radius: 20px;
				box-shadow: 0 4px 8px #ec1906;
				background-color: #ececec;
				display: flex;
				flex-direction: column;
				justify-content: space-around;
				.wrapper{
					margin: 0 auto;
					display: flex;
					justify-content: center;
					label{
						font-size: 20px;
						width: 110px;
						text-align: right;
					}
					input{
						background-color: white;
					}
				}
				.check-code{
					button{
						margin: auto 5px;
						width: 80px;
						height: 20px;
						background-color: white;
						border-radius: 5px;
					}
				}
				.commit{
					width: 80px;
					height: 30px;
					line-height: 30px;
					border-radius: 10px;
					font-weight: bold;
					background-color: #ec1906;
					text-align: center;
					margin: 0 auto;
				}
			}
		}
	}
	
</style>