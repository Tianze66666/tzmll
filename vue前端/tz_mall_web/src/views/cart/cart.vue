<template>
	<div class="shop-cart">
		<Shortcut></Shortcut>
		<Header></Header>
		<div class="goods" v-if='cartSumNums'>
			<div class="goods-num">
				全部商品&nbsp;&nbsp{{cartSumNums}};
			</div>
			<table>
				<tr>
					<th>
						<input type="checkbox" :checked='allChecked' @click="checkedAll" />
						全选
					</th>
					<th>商品</th>
					<th></th>
					<th>单价</th>
					<th>数量</th>
					<th>小计</th>
					<th>操作</th>
				</tr>
				<tr v-for="(item,index) in cartListData" :key="index">
					<td>
						<input type="checkbox" :checked='item.checked' @click="changeChecked(index)"/>
					</td>
					<td>
						<img :src="item.goods.image" alt="" />
					</td>
					<td @click="toDeail(item.goods.sku_id)">
						{{item.goods.name}}
					</td>
					<td>
						${{item.goods.p_price}}
					</td>
					<td>
						<el-input-number 
						v-model="item.nums"
						@change="(newvalue,oldvalue)=>handleChange(newvalue,oldvalue,item.sku_id,index)"
						:min="1"
						:max="100"
						label="描述文字"
						>
						</el-input-number>
					</td>
					<td>
						${{(item.goods.p_price * item.nums).toFixed(2)}}
					</td>
					<td @click="deleteOneGoods(index)">
						删除
					</td>
				</tr>
				
			</table>
			<div class="bottom-tool">
				<div class="tool-left">
					<input type="checkbox" :checked='allChecked' @click="checkedAll"/>
					全选
					<span class="delete-selected" @click="deleteGoods">删除选中商品</span>
					<span class="clear-cart" @click="clearCart">清理购物车</span>
				</div>
				<div class="tool-right">
					<span class="selected-goods">已选择<em>{{selectedGoodsCount}}</em>件商品</span>
					<span class="price-count">总价: <em>${{priceCount.toFixed(2)}}</em></span>
					<a href="#" class="go-order" @click="goOrder">去结算</a>
				</div>
				
			</div>
			
		</div>
		<div class="no-goods" v-if='!cartSumNums'><a href="/">购物车空空如也快去选购把</a></div>
	</div>

</template>

<script setup>
import { onMounted, ref ,watch} from 'vue';
import { useStore } from 'vuex';
import {useRouter} from 'vue-router'
import Shortcut from '@/components/common/Shortcut'
import Header from '@/components/home/Header'
import {getCartDetailData,updateGoodsNumData,deleteCartGoods} from '@/network/cart'
import {addcartData} from '@/utils/goods'
import {createOrderData} from '@/network/order'

	let router = useRouter()
	
	const toDeail = (skuId)=>{
		router.push('/detail/'+skuId)
	}

	let cartListData = ref([])
	let cartSumNums = ref(0)

	onMounted(()=>{
		// 后续进行代码的健壮性书写
		// 验证用户的登录状态
		getCartDetailData().then(res=>{
			if (res.data.status===false){
				return
			}
			console.log(res);
			cartListData.value = res.data
			// 计算商品总数
			for (let i in res.data){
				cartSumNums.value += res.data[i].nums
			}
		})
	})
	
	// 修改购物车商品的数量
	const store = useStore()
	const handleChange = (newvalue,oldvalue,skuId,index)=>{
		// 更新商品数量
		cartListData.value[index].nums = newvalue
		// if (newvalue>oldvalue){
		// 	cartSumNums.value+=1
		// 	if (cartListData.value[index].checked){
		// 		selectedGoodsCount.value += 1
		// 	}
		// }else{
		// 	cartSumNums.value-=1
		// 	if (cartListData.value[index].checked){
		// 		selectedGoodsCount.value -= 1
		// 	}
		// }
		
		let data = ref({
			sku_id:skuId,
			nums:newvalue,
		})
		updateGoodsNumData(data.value).then(res=>{
			store.dispatch('updataCart')
		})
	}
	
	// 全选与取消全选
	let allChecked = ref(false)
	const checkedAll = ()=>{
		if(allChecked.value === false){
			for(let i in cartListData.value){
				cartListData.value[i].checked=true
			}
			selectedGoodsCount.value = cartSumNums.value
			selectedItemsCount.value = cartListData.value.length
		}else{
			for(let i in cartListData.value){
				cartListData.value[i].checked=false
			}
			selectedGoodsCount.value = 0
			selectedItemsCount.value = 0
		}
		allChecked.value = allChecked.value?false:true
	}
	
	// 计算商品件数与总价格
	let selectedGoodsCount = ref(0)
	let priceCount = ref(0)
	// 选中的商品类别数量
	let selectedItemsCount = ref(0)
	// 计算商品总价
	watch(cartListData,(newvalue,oldvalue)=>{
		priceCount.value = 0
		selectedGoodsCount.value = 0
		cartSumNums.value = 0
		cartListData.value.forEach((element)=>{
			cartSumNums.value += element.nums
			if(element.checked===true){
				priceCount.value += element.goods.p_price*element.nums
				selectedGoodsCount.value += element.nums
			}
		})
	},{
		// 深度监听
		deep:true,
	})
	
	// 单个选中
	const changeChecked = (id)=>{
		cartListData.value[id].checked = !cartListData.value[id].checked
		if (cartListData.value[id].checked){
			selectedGoodsCount.value += cartListData.value[id].nums
			selectedItemsCount.value += 1
			if (selectedItemsCount.value == cartListData.value.length){
				allChecked.value = true
			}
			return
		}
		selectedGoodsCount.value -= cartListData.value[id].nums
		selectedItemsCount.value -= 1
		if (allChecked.value){
			allChecked.value = !allChecked.value
		}
	}
	
	// 删除商品
	let deleteGoodsList = ref([])
	let noDeleteGoodsList = ref([])
	const deleteGoods = ()=>{
		noDeleteGoodsList.value = []
		cartListData.value.forEach((element)=>{
			if(element.checked){
				deleteGoodsList.value.push(element.sku_id)
			}else{
				noDeleteGoodsList.value.push(element)
			}
		})
		if (deleteGoodsList.value.length === 0 ){
			alert('请先选择商品')
			return
		}

		let res = confirm('把选中商品永久移除购物车')
		if (res){
			deleteCartGoods(deleteGoodsList.value).then(res=>{
				if (res.status===3000){
					alert('删除成功')
					// location.reload()
					cartListData.value = []
					cartListData.value = noDeleteGoodsList.value
					store.dispatch('updataCart')
					cartSumNums.value = 0
					for (let i in cartListData.value){
						cartSumNums.value += cartListData.value[i].nums
					}
				}else{
					alert('删除失败,请稍后重试')
				}
			})
			
		}
	}
	
	// 删除单个商品
	const deleteOneGoods = (index)=>{
		let res = confirm('是否移除商品')
		if(res){
			deleteCartGoods(cartListData.value[index].sku_id)
			// console.log(cartListData.value[index].sku_id);
			cartListData.value.splice(index,1)
		}
	}
	
	// 清理购物车
	const clearCart = ()=>{
		let res = confirm('清空购物车')
		if (res){
			deleteGoodsList.value = []
			cartListData.value.forEach((element)=>{
				deleteGoodsList.value.push(element.sku_id)
			})
			deleteCartGoods(deleteGoodsList.value).then(res=>{
				if (res.status===3000){
					alert('删除成功')
					// location.reload()
					cartListData.value = []
					store.dispatch('updataCart')
					cartSumNums.value = 0
					location.href='/'
				}else{
					alert('删除失败,请稍后重试')
				}
			})
			
		}
	}
	
	// 订单结算
	let orderGoodsList = ref([])
	const goOrder = ()=>{
		for(let i in cartListData.value){
			if (cartListData.value[i].checked){
				orderGoodsList.value.push(cartListData.value[i])
			}
		}
		if (!orderGoodsList.value.length){
			alert('请选择商品')
			return
		}
		
		let orderData = ref({
			trade:{
				order_amount:priceCount.value,
			},
			goods:orderGoodsList.value
		})
		// 往后端发送网络请求
		let orderNo = ref("")
		createOrderData(orderData.value).then(res=>{
			orderNo.value = res.data.trade_no
			router.push('/order/'+orderNo.value)
			store.dispatch('updataCart')
		})
	}
	
	
</script>

<style lang="less" scoped>
	.shop-cart{
		.goods{
			width: var(--content-width);
			margin: 0 auto;
			.goods-num{
				color: #e2231a;
				font-size: 16px;
				font-weight: bold;
			}
			table{
				border-collapse: collapse;
				tr{
					border-bottom: 2px solid #f0f0f0;
					th{
						background-color: #f3f3f3;
						height: 45px;
						&:nth-child(1){
							width: 50px;
							padding-left: 10px;
						}
					}
					td{
						padding-top: 10px;
						padding-bottom: 10px;
						&:nth-child(1){
							text-align: center;
						}
						&:nth-child(3){
							width: 600px;
							padding-left: 20px;
							padding-right: 30px;
							&:hover{
								color: #e2231a;
								cursor: pointer;
							}
						}
						&:nth-child(4){
							width: 80px;
							text-align: center;

						}
						&:nth-child(5){
							width: 80px;
							text-align: center;
						}
						&:nth-child(6){
							width: 120px;
							text-align: center;
							font-weight: 700;
						}
						&:nth-child(7){
							width: 80px;
							text-align: center;
							&:hover{
								cursor: pointer;
								color: #e2231a;
							}
						}
						
						img{
							width: 80px;
							height: 80px;
							border: 1px solid #eeeeee;
						}
						
					}

				}
			}
			.bottom-tool{
				margin-top: 10px;
				border: 2px solid #f0f0f0;
				height: 50px;
				line-height: 50px;
				.tool-left{
					float: left;
					padding-left:20px ;
					span{
						padding: 0 10px;
						&:hover{
							color: #e2231a;
							cursor: pointer;
						}
					}
					.clear-cart{
						font-size: 14px;
						font-weight: bold;
					}
				}
				.tool-right{
					float: right;
					text-align: right;
					span{
						font-weight: 700;
						color: #acacac;
						em{
							color: #e2231a;
							font-weight: 700;
							padding: 0 5px;
						}
					}
					.price-count{
						em{
							font-size: 15px;

						}
					}
					.go-order{
						display: inline-block;
						width: 95px;
						height: 50px;
						background-color: #e2231a;
						color: white;
						line-height: 50px;
						text-align: center;
						font-size: 18px;
						font-weight: bold;
					}
				}
			}
		}
	
		.no-goods{
			width: var(--content-width);
			margin: 0 auto;
			font-size: 50px;
			padding-top: 50px;
			transform: translateX(25%);
		}
	}
	
</style>