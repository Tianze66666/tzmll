<template>
	<div class="main">
		<div class="shopcart" @click="toCart">
			<el-badge :value='$store.state.cartCount' class="item" >
					<span class="iconfont icon-gouwuche"></span>
			</el-badge>
			<span>我的购物车</span>
		</div>
	</div>
	
</template>

<script setup>
import { useRouter ,useRoute} from 'vue-router';
	const router = useRouter()
	const route = useRoute()
	const toCart = ()=>{
		router.push('/cart/detail/')
	}


	
</script>

<style lang="less" scoped>
@red:#e2231a;
	.main{
		height: 35px;
		margin-top: 45px;
		.shopcart{
			border: 1px solid #e3e4e5;
			width: 130px;
			height:35px;
			line-height: 35px;
			text-align: center;
			&:hover{
				cursor: pointer;
				border: 1px solid @red;
			}
			.item{
				height:25px;
				line-height: 25px;
				padding-top: 4px;
				span{
					color: @red;
					font-weight: 700;
					
				}
			}
			>span{
				margin-left: 20px;
				color: @red;
			}
		}
	}
</style>