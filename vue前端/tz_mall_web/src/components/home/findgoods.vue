<template>
	<div class="wrapper"> 
		<img src="@/assets/images/find-goods.png" alt="" />
		<div class='scroll-wrapper'>
			<vue3-seamless-scroll 
			:list="goodList" 
			class="scroll" 
			v-if="goodList.length"
			direction='left'
			:hover='true'
			:auto-play="true"
			:step='0.3'
			:auto-refresh="true"
			:wheel="true" 
			:isWatch="true"
			:limitScrollNum='5'
			:is-limit-scroll="true"
			:clone-node-num="2"
			>
				<div class="items">
					<div class="item" v-for="(item,index) in  goodList" :key="index">
						<div :class="['oneitem',index % 2 === 0 ? 'even' : 'odd']" @click="toDetail(item.sku_id)">
							<span class="dian1">{{item.name}}</span>
							<img :src="item.image" alt="">
						</div>
					</div>
				</div>
			</vue3-seamless-scroll>
		</div>
	</div>
</template> 

<script setup>
import { onMounted, ref } from 'vue';
import {getFindGoods} from '@/network/home'
import {useRouter} from 'vue-router';

const  goodList = ref([])
const router = useRouter()

onMounted(()=>{
	getFindGoods().then((res)=>{
		goodList.value = res.data
	})
})

const toDetail = function(skuId){
	router.push('/detail/'+skuId)
}



	
</script>

<style scoped lang="less">
@red:#e2231a;
.wrapper{
	height: 260px ;
	width: var(--content-width) ;
	margin: auto auto;
	overflow: hidden;
	display: flex;
	flex-direction: row;
	flex-direction: row !important;  /* 确保横向排列 */
	flex-wrap: nowrap !important;    /* 禁止换行 */
	.scroll-wrapper{
		overflow: hidden;
		height: 260px;
		width:1000px;
		margin-left: 10px;
		background-color: white;
		.scroll{
			overflow: hidden;
			height: 260px ;
			width:1000px;
			margin-left: 10px;
			width: 100%;
			.items{
				display: flex;
				// flex-direction: row;
				.item {
				    display: flex;
					flex-direction: column;
				    align-items: center;
				    justify-content: space-between;
				    padding: 3px 0;
					margin: 30px 10px;
					.oneitem{
						height:260px ;
						display: flex;
						margin-left: 5px;
						margin-right: 5px;
						&.even {
						  flex-direction: column;
						}
						&.odd {
						  flex-direction: column-reverse;
						}
						&:hover{
							cursor: pointer;
						}
						>img{
							width: 170px;
							height: 190px;
							object-fit: cover;
							border-radius: 10px;
							flex:  0 0;;
						}
						span{
							height: 20px;
							line-height: 20px;
							margin-bottom: 10px;
							flex: 1 1 30px;
						}
						>span:hover{
							color: @red;
					
						}
					}
				}
			}
		}
	}
	>img{
		width: 190px;
		height: 260px;
		cursor: pointer;
	}

}
	

  








</style>