<template>
	<div>
		<Shortcut></Shortcut>
		<Header></Header>
		<div class="all-goods">
			<div>
				<span>全部商品分类</span>
			</div>
		</div>
		<div class="all-goods-list">
			<div class="result-keyword">
				<span class="all-result-font">
					全部结果&nbsp;&nbsp;>&nbsp;&nbsp;
				</span>
				<span class="search-word">
					"{{keyword}}"
				</span>
			</div>
			<div class="goods-list" v-show="goodsListData">
				<div class="search-condition">
					<a href="#" v-for="(item,index) in orderTypes" :key="index" 
					@click="changeOrder(item.order,item.index)"
					:class="item.isActive?'current-condition':'not-current-condition'"
					><span>
						{{item.name}}
					</span>
					<img src="" alt="" />
					</a>
				</div>
				<div class="list-detail clearfix">
					<div class='every-goods fl' v-for="(item,index) in goodsListData" :key="index">
						<div>
							<img :src="item.image" class="goods-image" alt="" />
						</div>
						<div class="price">
							${{item.p_price}}
						</div>
						<div class="name cs dian2" @click="toDetail(item.sku_id)">
							{{item.name}}
						</div>
						<div class="comment_count">
							<span class="count">{{item.comment_count?item.comment_count:0}}</span>
							<span class='comment'>条评价</span>
						</div>
						<div class="shop-name">
							{{item.shop_name}}
						</div>
						<div class="add-cart cs" @click="addcartData(item.sku_id,1)">
							<img src="@/assets/images/cart/add-cart1.png" alt="" />
							加入购物车
						</div>
						
					</div>
				</div>
			</div>
			<div class="none" v-if="goodsListData.length == 0">
				<span>什么都没有，空空如也</span>
			</div>
		<div class="change-page">
			<div class="block">
				<el-pagination layout='prev , pager , next' 
				:total='goodsCount'
				:page-size="15"
				@current-change="handleCurrentChange"
				v-model:current-page="currentPage"
				></el-pagination>
			</div>
		</div>
			
			
		</div>
		
	</div>
</template>

<script setup>
import { onMounted, ref, computed ,watch} from 'vue';
import { useRoute,useRouter } from 'vue-router';
import Shortcut from '@/components/common/Shortcut'
import Header from '@/components/home/Header'
import {getGoodsListData , getKeywordCountData} from '@/network/goods'
import {addcartData} from '@/utils/goods'
	
	const router = useRouter()  // 全局路由对象
	const route = useRoute()  // 当前页面路由对象
	
	const toDetail = (skuId)=>{
		router.push('/detail/'+skuId)
	}
	
	let orderTypes = ref([
		{'index':1,'order':1,'name':'综合','isActive':true},
		{'index':2,'order':1,'name':'评论数','isActive':false},
		{'index':3,'order':2,'name':'价格','isActive':false},
	])
	let goodsListData = ref([])
	
	const getSearchData = function(keyword,page,order){
		getGoodsListData(keyword,page,order).then((res)=>{
			goodsListData.value = []
			for (let i  in res.data){
				goodsListData.value.push(JSON.parse(res.data[i]))
				
			}
		})
	}
	
	let goodsCount = ref(0)
	
	const getKeywordGoodsCount = (keyword)=>{
		getKeywordCountData(keyword).then(res=>{
			goodsCount.value = res
		})
	}
	let currentPage = ref(1)
	
	onMounted(()=>{
		let order = route.params.order
		if (order != 1){
			for(let i in orderTypes.value){
				orderTypes.value[i].isActive = false
				if(order == orderTypes.value[i].order){
					orderTypes.value[i].isActive = true
				}
			}
		}
		getKeywordGoodsCount(route.params.keyword)
		getSearchData(route.params.keyword,route.params.page,route.params.order)
		console.log(route.params.page);
		currentPage.value = parseInt(route.params.page) || 1
	}) 
	
	
	
	let keyword = computed(()=>{
		return route.params.keyword
	})
	
	let page  = computed(()=>{
		return route.params.page
	})
	
	let order  = computed(()=>{
		return route.params.order
	})
	
	watch(keyword,(newvalue,oldvalue)=>{
		getSearchData(newvalue,1,1)
		getKeywordGoodsCount(newvalue)
	})
	
	watch(page,(newvalue,oldvalue)=>{
		getSearchData(keyword.value,newvalue,order.value)
	})
	
	watch(order,(newvalue,oldvalue)=>{
		currentPage.value = 1
		getSearchData(keyword.value,1,newvalue)
	})
	
	const changeOrder = (cOrder,index)=>{
		// 点击完成之后，进行页面刷新
		router.push('/goods_list/'+route.params.keyword+'/'+1+'/'+cOrder)
		// 样式切换
		for(let i in orderTypes.value){
			if(orderTypes.value[i].index === index){
				orderTypes.value[i].isActive = true
			}else{
				orderTypes.value[i].isActive = false
			}
		}
	}

	const handleCurrentChange = (value)=>{
		console.log(value);
		router.push('/goods_list/'+keyword.value+'/'+value+'/'+order.value)
	}

</script>

<style lang="less" scoped>
	.all-goods{
		border-bottom: 2px solid #f30213;
		div{
			width: var(--content-width);
			margin: 0 auto;
			span{
				display: inline-block;
				background-color: #f30213;
				color:white;
				font-size: 14px;
				height:33px;
				width: 190px;
				line-height: 33px;
				text-align: center;
			}
		}
	}
	.all-goods-list{
		width: var(--content-width);
		margin: 0 auto;
		.result-keyword{
			margin-top: 20px;
			.all-result-font{
				color: #666;
				font-size: 12px;
			}
			.search-word{
				color: #666;
				font-weight: 700;
				font-size: 12px;
			}
		}
		.search-condition{
			margin-top: 10px;
			background-color: #f1f1f1;
			height: 40px;
			line-height: 40px;
			.current-condition{
				background-color: #e4393c;
				color: white;
				border: 1px solid #e4393c;
				img{
					content: url('@/assets/images/goods-list/down3.png');
				}

			}
			.not-current-condition{
				background-color: white;
				border: 1px solid #ddd;
				img{
					content: url('@/assets/images/goods-list/down1.png');
				}
				&:hover{
					border: 1px solid #e4393c;
					img{
						content: url('@/assets/images/goods-list/down2.png');
					}
				}
			}
			a{
				display: inline-block;
				text-align: center;
				height: 25px;
				line-height: 25px;
				width: 80px;
				text-align: center;
				font-size: 14px;
				img{
					width: 14px;
					height: 14px;
					margin-left:5px ;
				}
				&:first-child{
					margin-left: 10px;
				}
			}
			
		}
		.list-detail{
			.every-goods{
				margin-top: 10px;
				border: 1px solid #fff;
				width:238px;
				height: 400px;
				&:hover{
					border: 1px solid #e3e4e5;
				}
				.goods-image{
					margin-top: 5px;
					width: 220px;
					height: 220px;
				}
				.price{
					margin-top: 10px;
					color: #e4393c;
					font-size: 20px;
					margin-left: 5px;
				}
				.name{
					margin-top: 10px;
					font-size: 12px;
					color: #666;
					margin-left: 5px;
					&:hover{
						color:#e4393c;
					}
				}
				.comment_count{
					margin-top: 10px;
					margin-left: 5px;
					.count{
						color:#646fb0;
						font-weight: bold;
					}
					.comment{
						color: #a7a7a7;
						
					}
				}
				.shop-name{
					margin-top: 10px;
					margin-left: 5px;
					color:#999 ;
				}
				.add-cart{
					text-align: center;
					border: 1px solid #e4393c;
					img{
						width: 20px;
					}
					&:hover{
						color: #e4393c;
					}
				}
			}
		}
		.none{
			color: black;
			text-align: center;
			span{
				display: block;
				font-size: 60px;
				margin-top: 15%;
			}
		}
		.change-page{
			margin-top: 20px;
			margin-bottom: 20px;
			margin-left: 65%;
		}
	}

	
</style>