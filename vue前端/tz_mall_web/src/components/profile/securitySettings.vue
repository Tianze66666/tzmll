<template>
	<div class="basic-info">
		<table>
			<tr>
				<td class="table-key">
					旧密码:
				</td>
				<td class="table-value">
					<el-input type="password" v-model="oldpassword" placeholder="请输入密码"></el-input>
				</td>
			</tr>
			<tr>
				<td class="table-key">
					新密码:
				</td>
				<td class="table-value">
					<el-input type="password" v-model="newpassword" placeholder="请输入密码"></el-input>
				</td>
			</tr>
			<tr>
				<td class="table-key">
					再次输入新密码:
				</td>
				<td class="table-value">
					<el-input type="password" v-model="checkpassword" placeholder="请输入密码"></el-input>
				</td>
			</tr>
			<tr >
				<td class="submit">
					<el-button type="success" @click="submitChange">提交</el-button>
				</td>
			</tr>
			
		</table>
	</div>
</template>

<script setup>
import { ref } from 'vue';
import {changePassword} from '@/network/user'
import { useStore } from 'vuex';
	const store = useStore()

	let newpassword = ref('')
	let oldpassword = ref('')
	let checkpassword = ref('')
	
	const submitChange = ()=>{
		if (!newpassword.value){
			alert('不能为空')
			return
		}
		if (!oldpassword.value){
			alert('不能为空')
			return
		}
		if (!checkpassword.value){
			alert('不能为空')
			return
		}
		if(checkpassword.value!==newpassword.value){
			alert('两次密码不一致')
			return
		}
			
		let data = {
			new_password:newpassword.value,
			old_password:oldpassword.value
		}
		changePassword(data).then(res=>{
			if(res.status==4000){
				alert('修改成功')
			}else{
				alert('修改失败')
			}
		})
	}
	
</script>

<style lang="less" scoped>
	.basic-info{
		transform: translateY(-10px);
		width: 800px;
		height: 300px;
		background-color: #fff;
		border-radius: 20px;
		box-shadow:4px 8px #d0d0d0 ;
		table{
			padding-top: 20px;
			transform: translateX(25%);
			tr{
				height: 60px;
				.table-key{
					font-weight: bold;
					padding-left: 20px;
				}
				.table-value{
					
				}
				.submit{
					padding-top: 20px;
					transform: translateX(150%);
				}
			}
		}

	}
	
</style>