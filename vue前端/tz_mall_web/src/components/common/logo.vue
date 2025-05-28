<template>
	<div>
		<img src="@/assets/images/logo/logo-big.png" alt="" @click="toHome"/>
	</div>
</template>

<script setup>
	import {useRouter} from 'vue-router'
	const router = useRouter()
	const toHome = function(){
		router.push('/')
	}
	
</script>

<style scoped lang="less">
	div{
		line-height: 140px;
		&:hover{
			cursor: pointer;
		}
	}
	
	img{
		width: 100px;
		height: 100px;
		text-align: center;
	}
</style>