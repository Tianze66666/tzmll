<template>
	<div class="order">
		<div class="condition">
			<span v-for="(item,index) in orderStatusDict" 
			:key="index"
			@click="changeOrderStatus(item.payStatus)"
			:class="item.isActive?'is-active':''"
			>
			{{item.payName}}
			</span>
		</div>
		<table>
		
			<tr class="table-header">
				<th>订单详情</th>
				<th>收货人</th>
				<th>金额</th>
				<th>状态</th>
				<th>操作</th>
			</tr>
			<!-- 控制循环标签 -->
			<tbody class="order-info" v-for="(item,index) in goodsInfo" :key="index">
				<tr class="blank-tr"></tr>
				<tr class="info-header">
					<td class="order-num">
						<span>{{item.create_time}}</span>
						<span>订单号:</span>
						<b>{{item.trade_no}}</b>
					</td>
					<td colspan="4" class="img-td">
					  <el-popconfirm
						width="220px"
						confirm-button-text="确定"
						cancel-button-text="取消"
						title="确定删除这个订单吗"
						@confirm="deleteOrder(item.trade_no,index)"
					  >
						<template #reference>
						  <img src="@/assets/images/profile/delete.png" alt="" />
						</template>
					  </el-popconfirm>
					</td>
				</tr>
				<tr class="info-detail" v-for="(data,key) in item.order_info" :key="key">
					<td class="goods-detail clearfix">
						<a :href="'/detail/'+data.sku_id" target="_blank">
							<img :src="data.image" alt=""  class="fl"/>
							<div class="fl">
								<span class="dian2">{{data.name}}</span>
							</div>
						</a>
						<div class="goods-num fl">x{{data.goods_num}}</div>
					</td>
					<td :rowspan='item.order_info.length' v-if='key<1'>{{!item.signer_name?'未知收货人':item.signer_name}}</td>
					<td :rowspan='item.order_info.length' v-if='key<1'>{{item.order_amount}}</td>
					<td :rowspan='item.order_info.length' v-if='key<1'>{{switchStatus(item.pay_status)[0]}}</td>
					<td :rowspan='item.order_info.length' v-if='key<1' class="order-action">
						<span @click="toAction(item.pay_status,item.trade_no,item.order_amount,item.order_info,index)">{{switchStatus(item.pay_status)[1]}}</span>
					</td>
				</tr>
				<tr>{{item.trade_no}}</tr>
			</tbody>
		</table>
	</div>
		
	
</template>

<script setup>
import { onMounted, ref,reactive } from 'vue';
import {getAllOrders,updateOrderInfoData,createOrderData} from '@/network/order'
import { useRouter } from 'vue-router';
import { ElMessage } from 'element-plus';

	const router = useRouter()

	let goodsInfo = ref()

	const getOrderInfo = (data) => {
		getAllOrders(data).then(res=>{
			console.log(res.data);
			goodsInfo.value = res.data
		})
	}

	onMounted(()=>{
		getOrderInfo(-1)
	})
	
	// 筛选条件的变量
	const orderStatusDict = ref([
		{
			payStatus:-1,
			payName:'全部订单',
			isActive:true
		},
		{
			payStatus:0,
			payName:'待确认',
			isActive:false
		},
		{
			payStatus:1,
			payName:'待付款',
			isActive:false
		},
		{
			payStatus:2,
			payName:'待收货',
			isActive:false
		},
		{
			payStatus:3,
			payName:'已完成',
			isActive:false
		},
	])
	
	// 更改筛选条件
	const changeOrderStatus = (status) => {
		orderStatusDict.value.forEach((item)=>{
			if(item.payStatus==status){
				getOrderInfo(status);
				item.isActive = true
			}else{
				item.isActive = false
			}
		})
	}
	
	// 删除订单
	const deleteOrder=(tradeNo,index)=>{
		let updateData = ref({
			trade_no:tradeNo,
			is_delete:1
		})
		updateOrderInfoData(updateData.value).then(res=>{
			ElMessage.success({
				message:'删除成功',
				type:'success'
			})
			// location.reload()
			goodsInfo.value.splice(index,1)
		})
	}
	
	// 切换筛选
	const orderStatus = reactive({
		0:['待确认','确认订单'],
		1:['待付款','支付订单'],
		2:['待收货','确认收获'],
		3:['已完成','再次购买'],
	})
	const switchStatus = (stutas)=>{

		return orderStatus[stutas]
	}
	
	// 切换订单状态
	const toAction =(pay_status,trade_no,order_amount,orderInfo,index)=>{
		console.log(pay_status);
		if(pay_status==0){
			router.push('/order/'+trade_no)
		}else if(pay_status==1){
			router.push({
				name:'orderpay',
				query:{
					tradeNo:trade_no,
					orderAmount:order_amount
				}
			})
		}else if(pay_status==2){
			let updateData = ref({
				trade_no:trade_no,
				pay_status:3
			})
			console.log(goodsInfo);
			updateOrderInfoData(updateData.value).then(res=>{
				ElMessage.success({
					message:'收货成功',
					type:'success'
				})
				// location.reload()
				goodsInfo.value.splice(index,1)
			})
		}else{			
			let orderData = ref({
				trade:{
					order_amount:order_amount,
				},
				goods:orderInfo
			})
			let orderNo = ref('')
			createOrderData(orderData.value).then(res=>{
				orderNo.value = res.data.trade_no
				router.push('/order/'+orderNo.value)
			})
		}
	}
	
	
</script>

<style lang="less" scoped>
	.order{
		background-color: white;
		border-radius: 20px;
		box-shadow: 0px 4px 8px #d5d5d5;
		padding: 20px;
		.condition{
			span{
				margin-right: 20px;
				background: linear-gradient(to right,#e2231a) no-repeat right bottom ;
				background-size:0 2px;
				transition:0.3s;
				padding-bottom: 2px;
				&:hover{
					cursor: pointer;
					color: #e2231a;
					background-position-x:left;
					background-size:100% 2px
				}
			}
			.is-active{
				color: #e2231a;
				background: linear-gradient(to right,#e2231a) no-repeat right bottom ;
				background-size:100% 2px;
				font-weight: bold;
			}
		}
		table{
			width: 900px;
			border-collapse:collapse;
			margin-top: 20px;
			.table-header{
				border: 1px solid #e5e5e5;
				background-color: #f5f5f5;
				height: 35px;
				th:first-child{
					width: 500px;
				}
				th:not(:first-child){
					width: 100px;
				}
			}
			.order-info{
				// border: 1px solid #e5e5e5;
				.blank-tr{
					height: 20px;
				}
				.info-header{
					border: 1px solid #e5e5e5;
					background-color: #f5f5f5;
					height: 30px;
					.order-num{
						span{
							margin-left: 30px;
							b{
								color: #333;
							}
						}
					}
					.img-td{
						text-align: right;
						padding-right: 40px;
						img{
							width: 15px;
							height: 15px;
							&:hover{
								cursor: pointer;
								content:url('@/assets/images/profile/delete-red.png');
							}
						}

					}
				}
				.info-detail{
					border: 1px solid #e5e5e5;
					.goods-detail{
						border: 1px solid #e5e5e5;
						a{
							img{
								width: 60px;
								height: 60px;
								margin-left: 10px;
							}
						
							div{
								margin-left:10px ;
								width: 300px;
								padding-top: 15px;
								span{
									
								}
							}
						}
						.goods-num{
							padding-top: 15px;
							margin-left: 50px;
							font-size: 14px;
						}
					}
					td{
						text-align: center;
						border: 1px solid #e5e5e5;
					}
					.order-action{
						span{
							border: 1px solid #ddd;
							background-color: #f5f5f5;
							display: inline-block;
							width: 90px;
							height: 30px;
							line-height: 30px;
							text-align: center;
							&:hover{
								cursor: pointer;
								color:#e2231a;
								border: 1px solid #e2231a;
							}
						}

					}
				}
			}

		}
	}
	
</style>