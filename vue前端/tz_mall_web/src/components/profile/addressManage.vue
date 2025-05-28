<template>
	<div class="address">
		<div class="addAddressButton" @click="addAddressDialogFormVisible = true">新增地址</div>
		<!--地址页，从后端数据库拿到数据进行循环 -->
		<div class="info" v-for="(item,index) in allAddress" :key="index">
			<div class=" clear-fix">
				<span class="title fl"> {{item.signer_name}}</span>
				<div class="default fl" v-if="item.default">默认地址</div>
				<img class="fr " src="@/assets/images/profile/deletex.png" alt="" @click="deleteAddress(index)" />
			</div>
			<table>
				<tr>
					<td class="table-key">收货人:</td>
					<td class="table-value">{{item.signer_name}}</td>
				</tr>
				<tr>
					<td class="table-key">所在地区:</td>
					<td class="table-value">{{item.district}}</td>
				</tr>
				<tr>
					<td class="table-key">收货地址:</td>
					<td class="table-value">{{item.signer_address}}</td>
				</tr>
				<tr>
					<td class="table-key">手机:</td>
					<td class="table-value">{{item.telphone}}</td>
				</tr>
				<tr class="edit">
					<td class="table-key"></td>
					<td class="table-value" @click="editAddress(item.id)"><span>编辑</span></td>
				</tr>
			</table>
		
		<!--新增收获地址弹窗框 -->
		
		</div>
		  <el-dialog v-model="addAddressDialogFormVisible" title="新增收货地址" width="500">
		    <el-form :model="form">
		      <el-form-item label="收货人" :label-width="formLabelWidth">
		        <el-input v-model="form.signer_name" autocomplete="off" />
		      </el-form-item>
			  <el-form-item label="所在地区" :label-width="formLabelWidth">
			    <el-input v-model="form.district" autocomplete="off" />
			  </el-form-item>
			  <el-form-item label="收货地址" :label-width="formLabelWidth">
			    <el-input v-model="form.signer_address" autocomplete="off" />
			  </el-form-item>
			  <el-form-item label="联系电话" :label-width="formLabelWidth">
			    <el-input v-model="form.telphone" autocomplete="off" />
			  </el-form-item>
			  <el-form-item label="是否默认地址" :label-width="formLabelWidth">
			    <el-switch v-model="form.default" active-color="#13ce66" inactive-color="#ff4949"></el-switch>
			  </el-form-item>
		    </el-form>
		    <template #footer>
		      <div class="dialog-footer">
		        <el-button @click="addAddressDialogFormVisible = false">取消</el-button>
		        <el-button type="primary" @click="saveNewAddress">
					确认
		        </el-button>
		      </div>
		    </template>
		  </el-dialog>
		  
		  <!-- 编辑地址弹出框 -->
		    <el-dialog v-model="editAddressDialogFormVisible" title="编辑收货地址" width="500">
		      <el-form :model="editAddressInfo">
		        <el-form-item label="收货人" :label-width="formLabelWidth">
		          <el-input v-model="editAddressInfo.signer_name" autocomplete="off" />
		        </el-form-item>
		  	  <el-form-item label="所在地区" :label-width="formLabelWidth">
		  	    <el-input v-model="editAddressInfo.district" autocomplete="off" />
		  	  </el-form-item>
		  	  <el-form-item label="收货地址" :label-width="formLabelWidth">
		  	    <el-input v-model="editAddressInfo.signer_address" autocomplete="off" />
		  	  </el-form-item>
		  	  <el-form-item label="联系电话" :label-width="formLabelWidth">
		  	    <el-input v-model="editAddressInfo.telphone" autocomplete="off" />
		  	  </el-form-item>
		  	  <el-form-item label="是否默认地址" :label-width="formLabelWidth">
		  	    <el-switch v-model="editAddressInfo.default" active-color="#13ce66" inactive-color="#ff4949"></el-switch>
		  	  </el-form-item>
		      </el-form>
		      <template #footer>
		        <div class="dialog-footer">
		          <el-button @click="editAddressDialogFormVisible = false">取消</el-button>
		          <el-button type="primary" @click="updateAddressInfo">
		  			更新
		          </el-button>
		        </div>
		      </template>
		    </el-dialog>
		
	</div>
</template>

<script setup>
import { onMounted, reactive, ref } from 'vue'
import {addAddressData,getAllAddressData,editAddressData,deleteAddressData} from '@/network/address'
	
	let addAddressDialogFormVisible = ref(false)
	const formLabelWidth = '140px'
	const form = reactive({
		signer_name:"",
		district:"",
		signer_address:"",
		telphone:"",
		default:false,
	})
	
	const saveNewAddress = ()=>{
		addAddressData(form).then(res=>{
			console.log(res);
			if(res.status===7000){
				getAllAddress()
				alert('保存成功')
			}
		})
		addAddressDialogFormVisible.value = false
	}
	
	let allAddress = ref([
		{
			id:"",
			signer_name:"",
			district:"",
			signer_address:"",
			telphone:"",
			default:false,
		}
	])
	const getAllAddress = ()=>{
		getAllAddressData().then(res=>{
			allAddress.value = res.data
		})
	}
	
	onMounted(()=>{
		getAllAddress()
	})
	
	// 编辑地址
	let editAddressDialogFormVisible = ref(false)
	let editAddressInfo = reactive({
					id:'',
					signer_name:"",
					district:"",
					signer_address:"",
					telphone:"",
					default:false,
				})
	const editAddress=(id)=>{
		allAddress.value.forEach((item)=>{
			if(item.id == id){
				// editAddressInfo = item
				Object.assign(editAddressInfo, item)
			}
		})
		editAddressDialogFormVisible.value = true
	}
	
	const updateAddressInfo = ()=>{
		editAddressData(editAddressInfo).then(res=>{
			if (editAddressInfo.default === true){
				allAddress.value.forEach((item)=>{
					item.default = false
				})
			}
			for(let i in allAddress.value){
				if(allAddress.value[i].id === editAddressInfo.id){
					allAddress.value[i] = JSON.parse(JSON.stringify(editAddressInfo))
				}
			}
			allAddress.value.sort((a, b) => {
			  return b.default - a.default
			})
			
			// getAllAddress()
		})
		// window.location.reload()
		
		editAddressDialogFormVisible.value = false
	}
	
	// 删除地址
	const deleteAddress = (index)=>{
		// console.log(allAddress.value[index].id);
		deleteAddressData({id:allAddress.value[index].id}).then(res=>{
			if (res.status===7000){
				allAddress.value.splice(index,1)
			}
		})
	}

</script>

<style lang="less" scoped>
	.address{
		padding-top: 20px;
		padding-left: 20px;
		padding-bottom: 20px;
		background-color: #fff;
		width: 870px;
		border-radius: 20px;
		box-shadow: 0px 4px 8px #d6d6d6;
		.addAddressButton{
			width: 115px;
			height: 30px;
			line-height: 30px;
			text-align: center;
			background-color: #f0f9e9;
			border: 1px solid #bfd6af;
			font-weight: 700;
			&:hover{
				cursor: pointer;
			}
		}
		.info{
			margin-top: 10px;
			border: 2px solid #e6e6e6;
			border-radius: 20px;
			width: 830px;
			height: 180px;
			>div{
				padding: 10px;
			}
			.title{
				font-size: 14px;
				color: #666;
			}
				
			.default{
				margin-left: 20px;
				width: 55px;
				height: 20px;
				text-align: center;
				line-height: 20px;
				background-color: #ffaa45;
				color: white;
			}
			img{
				width: 16px;
				height: 16px;
				&:hover{
					cursor: pointer;
				}
			}
		}
		table{
			margin-left: 20px;
			margin-top: 20px;
			tr{
				font-size: 15px;
				// transform: translateX(-80%) translateY(10px);
				margin-left: 0px;
				td{
					padding-bottom: 10px;
				}
			}
			.table-key{
				text-align: right;
				color: #999;
			}
			.table-value{
				padding-left: 10px;
				width: 710px;
			}
			.edit{
				transform: translateY(-40%) translateX(-1%);
				text-align: right;
				color: #55e075;
				font-weight: bold;

				.table-value{
					>span:hover{
						cursor: pointer;
						color: #e2231a;
				}
				}
			}
		}
		
		
	}
	
</style>