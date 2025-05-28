<template>
	<div class="main">
		<div class="content">
			<div class="logo">
				<logo></logo>
			</div>
			<div class="search-box">
				<div class="input-search">
					<searchbox></searchbox>
				</div>
				<div  class='shop-cart'>
					<Shopcart></Shopcart>
				</div>
			</div>
			<div class="right">
				<img src="@/assets/images/header-right.png" alt="" />
			</div>
		</div>
	</div>
</template>

<script setup>
	import logo from '@/components/common/logo'
	import searchbox from '@/components/home/searchbox'
	import Shopcart from '@/components/home/shopCart'
</script>

<style lang="less" scoped>
	.main{
		position: relative;
	}
	.main .content{
		display: flex;
		flex-direction: row;
		justify-content: space-around;
		// border:1px solid black;
		width:var(--content-width);
		height:140px;
		margin:0 auto;	
	}
	.main .search-box{
		transform: translateX(-5%);
		width: 800px;
		display: flex;
		flex-direction: row;
		justify-content: space-around;
		.shop-cart{
			transform: translateX(15%);
		}
	}
	.main .right{
		line-height: 140px;
	}
	
	.main .right img{
		height: 140px;
	}
	
</style>