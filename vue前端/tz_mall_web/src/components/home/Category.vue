<template>
	<div class="category1">
		<!--{{goods}} -->
		<div class="wrapper">
			<div class="goods" v-for="(item,index) in goods" :key='index' @click="toDetail(item.sku_id)">
				<div class="first-row">
					<img :src="item.image" alt="" />
				</div>
				<div class="second-row dian2">
					{{item.name}}
				</div>
				<div class="third-row">
					<small>$</small>
					<span>{{item.jd_price}}</span>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { onMounted, ref, watch} from 'vue';
import {getCategoryGoods} from '@/network/home'
import {useRouter} from 'vue-router'

	const router = useRouter()
	let categoryId = defineProps(['categoryId'])	

	let goods = ref([])
	
	// 声明变量用来存储现在是多少页
	let page=ref(1)
	
	const toDetail = (skuId)=>{
		router.push('/detail/'+skuId)
	}
	
	onMounted(()=>{
		getCategoryData(categoryId.categoryId,1)
	})
	
	const getCategoryData = function(categoryId,page){
		getCategoryGoods(categoryId,page).then((res)=>{
			let serverData = res.data
			for (let i in serverData){
				// let jsonData = JSON.parse(serverData[i])
				goods.value.push(serverData[i])
			}
		})
	}
	watch(categoryId,(newValue,oldValue)=>{
		goods.value = []
		getCategoryData(newValue.categoryId,1)
		page.value = 1
	})
	
	const windomScroll = ()=>{
		// 可视区域的高度
		let clientHeight = document.documentElement.clientHeight
		// 滚动条在文档中的高度的位置
		let scrollTop = document.documentElement.scrollTop
		// 所有内容的高度
		let scrollHeight = document.documentElement.scrollHeight
		
		if(clientHeight+scrollTop>=scrollHeight){
			page.value += 1
			getCategoryData(categoryId.categoryId,page.value)
		}
	}
	
	window.addEventListener('scroll',windomScroll)
	
	
</script>

<style scoped lang="less">
@red:#e2231a;
	.category1{
		width: var(--content-width);
		margin: 0 auto;
		margin-top: 10px;
		.wrapper{
			display: grid;
			grid-template-columns: repeat(5, 1fr);
			row-gap: 8px; 
			column-gap: 3px; 
			// grid-template-rows: 250px 250px 250px 250px ;
			.goods{
				width: 230px;
				height: 250px;
				background-color: #fff;
				.first-row{
					text-align: center;
					margin-bottom: 5px;
					img{
						margin-top: 5px;
						height: 150px;
						width: 150px;
					}
				}
				.second-row{
					width: 190px;
					height: 39px;
					font-size: 14px;
					color:#666;
					padding:  0 20px;
					overflow: hidden;
					&:hover{
						color:@red;
						cursor: pointer;
					}
				}
				.third-row{
					text-align: left;
					font-size: 18px;
					color: @red;
					margin-top: 10px;
					margin-left: 20px;
				}
			}
		}
	}
	
	
</style>