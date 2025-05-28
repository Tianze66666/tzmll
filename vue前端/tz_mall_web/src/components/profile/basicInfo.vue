<template>
	<div class="basic-info">
		<table>
			<tr>
				<td class="table-key">
					昵称:
				</td>
				<td class="table-value">
					<el-input v-model="inputName" placeholder="请输入名称"></el-input>
				</td>
			</tr>
			<tr >
				<td class="table-key">
					性别:
				</td>
				<td class="table-value">
					<el-radio v-model='gender' label="男" size="default">男</el-radio>
					<el-radio v-model='gender' label="女" size="default">女</el-radio>
					<!-- <el-radio v-model='gender' label="保密" size="default">保密</el-radio> -->
				</td>
			</tr>
			<tr >
				<td class="table-key">
					生日:
				</td>
				<td class="table-value">
					<el-date-picker v-model="dateValue" type="date" placeholder="请选择日期"></el-date-picker>
				</td>
			</tr>
			<tr >
				<td class="submit">
					<el-button type="success" @click="submitDetail">提交</el-button>
				</td>
			</tr>
		</table>
	</div>
</template>

<script setup>
import { ref,onMounted } from 'vue';
import {getUserDetailRequest,updateUserInfo} from '@/network/user'
import {useStore} from 'vuex';

	let inputName = ref('')
	let gender = ref('男')
	let dateValue = ref('2020-10-10')
	
	const store = useStore()
	
	onMounted(()=>{
		getUserDetailRequest().then((res)=>{
			inputName.value = res.data.name
			gender.value = res.data.gender?'男':'女'
			dateValue.value = res.data.birthday
		})
	})
	
	const submitDetail = ()=>{
		let userInfo = {
			name:inputName.value,
			gender:gender.value==='男'?true:false,
			birthday:JSON.parse(JSON.stringify(dateValue.value))
		}
		updateUserInfo(userInfo).then(res=>{
			if(res.status === 4000){
				alert('修改成功')
				store.commit('setUsername',inputName)
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