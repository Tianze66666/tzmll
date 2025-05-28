<template>
	<div>
		<shortcut></shortcut>
		<div class="order-pay">
			<div class="header">
				<div class="title clearfix">
					<div class="logo fl">
						<logo></logo>
					</div>
					<div class="shop-name fl">tzmall</div>
					<div class="name fl">支付页</div>
					<div class="cart fr">
						<shopCart></shopCart>
					</div>
				</div>
			</div>
			<div class="order-info">
				<div class="order-num">提交成功，订单号:
					<span>{{tradeNo}}</span>
				</div>	
				<div class="pay-mode">
					<div>
						应付金额
						<span class="pay-count">{{orderAmount}}</span>元
					</div>
					<img src="@/assets/images/order/alipay.png" alt="" />支付宝支付
				</div>
				<div class="pay-order">
					<button class="pay-order-button" @click="toAlipay">立即支付</button>
				</div>
			</div>
			
			
		</div>
		
	</div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import shortcut from '@/components/common/Shortcut'
import logo from '@/components/common/logo'
import { useRoute,useRouter } from 'vue-router';
import {toAlipayPage} from '@/network/order'
	
	const route = useRoute()
	let tradeNo = ref()
	let orderAmount = ref()
	
	onMounted(()=>{
		tradeNo.value = route.query.tradeNo
		orderAmount.value = route.query.orderAmount
	})
	
	const toAlipay = ()=>{
		let orderData = ref({
			tradeNo:tradeNo.value,
			orderAmount:orderAmount.value
		})
		
		let pay_url = ref('')
		toAlipayPage(orderData.value).then(res=>{
			pay_url.value = res.alipay
			window.location.href=pay_url.value
		})
	}


	
</script>

<style lang="less" scoped>
	.order-pay{
		width: 800px;
		margin: 0 auto;
		.header{
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
			}
		}
		.order-info{
			margin-top: 50px;
			.order-num{
				font-size: 20px;
			}
			.pay-mode{
				font-size: 16px;
				margin-top: 20px;
				padding: 20px;
				span{
					color: #e33f48;
					font-weight: bold;
				}
			}
			.pay-order{
				text-align:right;
				margin-top: 20px;
				.pay-order-button{
					margin-right: 200px;
					width: 135px;
					height: 35px;
					background-color: #f00c0c;
					color: white;
					border-radius: 5px;
				}
			}
		}
	}
	
</style>