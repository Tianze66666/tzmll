<template>
	<div >
		<shortcut></shortcut>
		<div class="order">
			<div class="header">
				<div class="title clearfix">
					<div class="logo fl">
						<logo></logo>
					</div>
					<div class="shop-name fl">tzmall</div>
					<div class="name fl">结算页</div>
					<div class="cart fr">
						<shopCart></shopCart>
					</div>
				</div>
			</div>
			<div class="order-info">
				<div class=" clearfix">
					<div class="step-title fl">
						<h3>收货人信息</h3>
					</div>
					<div class="add-address fr">
						新增收获地址
					</div>
				</div>

				<!-- 循环位置 -->
				<div class="step-context" v-for="(item,index) in allAddresses" :key='index'>
					<span class="address-name " 
					:class="item.selected?'selected':''" 
					@click="changeSelectd(item.id)"
					>{{item.signer_name}}</span>
					<span class="address-info">{{item.signer_address}}</span>
					<span class="address-phone">{{item.telphone}}</span>
					<span class="address-default" v-show="item.default==1">默认地址</span>
				</div>
				<hr />
				<div class="step-title">
					<h3>支付方式</h3>
				</div>
				<div class="step-context">
					<div class="pay-mode selected">支付宝</div>
				</div>
				<hr />
				<div class="step-title">
					<h3>送货清单</h3>
				</div>
				<div class="step-context clearfix">
					<div class="post-mode fl">
						<div>配送方式</div>
						<div class="selected">顺丰快递</div>
						<div>标准达: <i>预计2050年送达</i></div>
					</div>
					<div class="goods-list fl">
						<!-- 循环的地方 -->
						<div v-for="(item,index) in goodsInfo" :key="index">
							<div class="goods-shop-name">
								商家:{{item.shop_name}}
							</div>
							<div>
								<img :src="item.image" alt="" />
								<span class="goods-name">{{item.name}}</span>
								<span class="goods-price">{{item.p_price}}</span>
								<span class="goods-num">x{{item.goods_num}}</span>
							</div>
						</div>
					</div>
				</div>
				
			</div>
			<div class="trade-foot">
				<span>应付金额</span>
				<span class="count-price">{{orderAmount}}</span>
			</div>
			<div class="commit-order">
				<div class="commit-order-button" @click="submitOrder">提交订单</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { onMounted ,ref} from 'vue';
import {getAllAddressData} from '@/network/address'
import {getAllOrdersByTradeNo}	from '@/network/order'
import {useRoute} from 'vue-router'
import shortcut from '@/components/common/Shortcut'
import logo from '@/components/common/logo'
import {updateOrderInfoData} from '@/network/order'
import { useRouter } from 'vue-router';

	const router = useRouter()

	let allAddresses = ref()
	let goodsInfo = ref()
	let tradeNo = ref()
	let orderAmount = ref(0)

	const route = useRoute()
	
	onMounted(()=>{
		tradeNo.value = route.params.trade_no
		getAllAddressData().then(res=>{
			allAddresses.value = res.data
			allAddresses.value.forEach((item)=>{
				if(item.default===true){
					item.selected = true
					selectAddressId.value = item.id
				}else{
					item.selected = false
				}
			})
		})
		getAllOrdersByTradeNo(tradeNo.value).then(res=>{
			goodsInfo.value = res.data.order_info
			orderAmount.value = res.data.order_amount
		})
	})
	
	// 切换地址
	let selectAddressId = ref('')
	const changeSelectd = (id) => {
		allAddresses.value.forEach((item)=>{
			if(item.id === id){
				item.selected = true
				selectAddressId.value = id
			}else{
				item.selected = false
			}
		})
	}
	
	const submitOrder = () => {
		let updateData = ref({
			address_id:selectAddressId.value,
			trade_no:tradeNo.value,
			pay_status:1
		})
		updateOrderInfoData(updateData.value).then(res=>{
			if(res.status==6000){
				router.push({
					name:'orderpay',
					query:{
						tradeNo:tradeNo.value,
						orderAmount:orderAmount.value
					}
				})
			}
		})
		
		
	}
	
	
</script>

<style lang="less" scoped>
	.order{
		width: var(--content-width);
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
		.title{
			height: 42px;
			font-size: 16px;
			line-height: 42px;
		}
		
		.order-info{
			border: 1px solid #f0f0f0;
			margin-top: 20px;
			.step-title{
				height: 40px;
				line-height: 40px;
				padding-left: 20px;
				h3{
					font-size: 14px;
					font-weight: bold;
				}
			}
			.add-address{
				color: #005ea7;
				padding-right: 20px;
				padding-top: 20px;
				&:hover{
					color: #df0000;
					cursor: pointer;
				}
			}
			.step-context{
				padding-left: 20px;
				.address-name{
					display: inline-block;
					width: 145px;
					height: 30px;
					border: 2px solid #ddd;
					text-align: center;
					line-height: 30px;
					margin-bottom: 15px;
					&:hover{
						cursor: pointer;
					}
				}
				.address-info{
					margin-left: 30px;
				}
				.address-phone{
					margin-left: 30px;
				}
				.address-default{
					margin-left: 30px;
					background-color: #999;
					width: 60px;
					height: 20px;
					display: inline-block;
					text-align: center;
					line-height: 20px;
					border-radius: 5px;
					color: white;
					font-weight: bold;
					&:hover{
						cursor: pointer;
					}
				}
				.pay-mode{
					width: 100px;
					height: 30px;
					line-height: 30px;
					text-align: center;
					border: 2px solid #f0f0f0;
					&:hover{
						border: 2px solid #df0000;
						cursor: pointer;
					}
				}
				.selected{
					border: 2px solid #df0000;
					background-image:url('@/assets/images/order/address-selected.png') ;
					background-position:103%;
					background-repeat: no-repeat;
					background-size:35px ;
				}
				.post-mode{
					width: 375px;
					background-color: #f7f7f7;
					padding: 10px 0 10px 20px;
					div:nth-child(1){
						font-weight: bold;
					}
					div:nth-child(2){
						margin-top: 20px;
						font-weight: bold;
						width: 145px;
						height: 30px;
						line-height: 30px;
						text-align: center;
						&:hover{
							cursor: pointer;
						}
					}
					div:nth-child(3){
						margin-top: 5px;
					}
				}
				.goods-list{
					width: 780px;
					background-color: #f3fbfe;
					.goods-shop-name{
						margin-top: 10px;
						margin-left: 20px;
						font-weight: 700;
					}
					img{
						width: 85px;
						height: 85px;
						margin-top: 10px;
						margin-left: 20px;
						border: 1px solid #f0f0f0;
						background-color: white;
					}
					.goods-name{
						width: 570px;
						margin-left: 20px;
					}
					.goods-price{
						margin-left: 20px;
						color: #df0000;
						font-weight: 700;
					}
					.goods-num{
						margin-left: 20px;
					}
				}

			}
			hr{
				width: 1160px;
				border: 1px solid #f0f0f0;
			}

			
		}
		.trade-foot{
			background-color: #f4f4f4;
			margin-top: 30px;
			height: 50px;
			line-height: 50px;
			text-align: right;
			padding-right: 40px;
			.count-price{
				margin-left: 30px;
				color: #f00f0c;
				font-size: 16px;
				font-weight: bold;
			}
			.count-price::before{
				content: '$';
			}
		}
		.commit-order{
			margin-top: 10px;
			margin-bottom: 30px;
			text-align: right;
			margin-right: 40px;
			.commit-order-button{
				height: 35px;
				width: 135px;
				text-align: center;
				line-height: 35px;
				font-size: 16px;
				background-color: #df0000;
				color: white;
				font-weight: bold;
				display: inline-block;
				margin-top: 20px;
				border-radius: 5px;
				&:hover{
					cursor: pointer;
				}
			}
		}
	}
	
</style>