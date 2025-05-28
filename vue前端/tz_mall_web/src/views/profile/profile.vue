<template>
	<div >
		<Shortcut></Shortcut>
		<div class="profile">
			<div class="header">
				<div class="title clearfix">
					<div class="logo fl">
						<logo></logo>
					</div>
					<div class="shop-name fl">tzmall</div>
					<div class="name fl">个人中心</div>
					<div class="cart fr">
						<shopCart></shopCart>
					</div>
				</div>
			</div>
			<div class="main clearfix">
				<div class="content">
					<div class="left-menu fl">
						<div class="basic" 
						:class="activeIndex==1?'active-menu':''"
						@click="changeComponent(1)"
						>基本信息</div>
						<div class="address" 
						:class="activeIndex==2?'active-menu':''"
						@click="changeComponent(2)"
						>地址管理</div>
						<div class="order"
						:class="activeIndex==3?'active-menu':''"
						@click="changeComponent(3)"
						>我的订单</div>
						<div class="security"
						:class="activeIndex==4?'active-menu':''"
						@click="changeComponent(4)"
						>安全设置</div>
					</div>
					<div class="right-content fl">
						<component :is="activeComponentName"></component>
					</div>
				</div>

			</div>
		</div>
	</div>
</template>

<script setup>
import Shortcut from '@/components/common/Shortcut'
import shopCart from '@/components/home/shopCart'
import logo from '@/components/common/logo'
import {useRouter,useRoute}	from 'vue-router'
import { onMounted, ref,shallowRef } from 'vue'
import basicInfo from '@/components/profile/basicInfo'
import addressManage from '@/components/profile/addressManage'
import securitySettings from '@/components/profile/securitySettings'
import myOrder from '@/components/profile/myOrder'

	// export default{
	// 	name:'profile',
	// 	setup(){
	// 		const router = useRouter()
	// 		const route = useRoute()
	// 		let activeComponentName = ref('basicInfo')
	// 		let activeIndex = ref(route.query.activeIndex || 1)
	// 		let activeComponent = ref([
	// 			{index:1,componentName:'basicInfo'},
	// 			{index:2,componentName:'addressManage'},
	// 			{index:3,componentName:'myOrder'},
	// 			{index:4,componentName:'securitySettings'},
	// 		])
			
	// 		const changeComponent = (index)=>{
	// 			activeIndex.value = index
	// 			activeComponent.value.forEach((item)=>{
	// 				if(item.index===index){
	// 					activeComponentName.value = item.componentName
	// 				}
	// 			})
	// 			router.push('profile?activeIndex='+activeIndex.value)
	// 		}
	// 		return {
	// 			activeComponentName,
	// 			activeIndex,
	// 			activeComponent,
	// 			changeComponent
	// 		}
	// 	},
	// 	components:{
	// 		basicInfo,
	// 		addressManage,
	// 		securitySettings,
	// 		myOrder,
	// 		Shortcut,
	// 		shopCart,
	// 		logo
	// 	}
	// }
	
	const router = useRouter()
	const route = useRoute()
	let activeComponentName = shallowRef(basicInfo)
	let activeIndex = ref(parseInt(route.query.activeIndex) || 1)
	let activeComponent = shallowRef([
		{index:1,componentName:basicInfo},
		{index:2,componentName:addressManage},
		{index:3,componentName:myOrder},
		{index:4,componentName:securitySettings},
	])
	
	const changeComponent = (index)=>{
		activeIndex.value = index
		// activeComponent.value.forEach((item)=>{
		// 	if(item.index===index){
		// 		activeComponentName.value = item.componentName
		// 	}
		// })
		activeComponentName.value = activeComponent.value[index-1].componentName
		router.push('profile?activeIndex='+activeIndex.value)
	}
	
	onMounted(()=>{
		activeComponent.value.forEach((item)=>{
			if(item.index===activeIndex.value){
				activeComponentName.value = item.componentName
			}
		})
			
	})





</script>

<style lang="less" scoped>
	
	.profile{
		.header{
			border-bottom: 2px solid #f00c0c;
			height: 120px;
			line-height: 120px;
			.title{
				width: var(--content-width);
				height: 80px;
				margin: 0 auto;
				line-height: 80px;
				.logo{
					height: 40px;
				}
				.shop-name{
					font-size: 40px;
					font-weight: bold;
					color: #f00f0c;
					margin-left: 10px;
					margin-top: 30px;
				}
				.name{
					font-size: 25px;
					margin-left: 10px;
					margin-top: 30px;
				}
				.cart{
					margin-top: 10px;
				}
			}
		}
		>.main{
			background-color: #f5f5f5;
			.content{
				width: var(--content-width);
				margin: 0 auto;
				.left-menu{
					height: 800px;
					margin-top: 20px;
					color: #333;
					font-size: 14px;
					margin-bottom: 20px;
					div{
						margin-top: 20px;
						background:linear-gradient( to right, #e93854) no-repeat bottom;						background-size: 0 2px; 
						background-size: 0 2px;
						transition: 0.3s;
						&:hover{
							cursor: pointer;
							color: #f00c0c;
							background-position-x:left;						
							background-size: 100% 2px;	
						}
					}
					.active-menu{
						color: #f00c0c;
						background:linear-gradient( to right, #e93854) no-repeat bottom;						background-size: 0 2px;
						background-size: 100% 2px;
					}
				}
				.right-content{
					margin-top: 50px;
					margin-left: 50px;
					margin-bottom: 20px;
				}
				
			}

			
		}
	}
	
</style>