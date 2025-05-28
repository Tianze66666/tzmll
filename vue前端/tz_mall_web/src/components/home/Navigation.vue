<template>
	<div class="nav">
		<div class="main">
			<leftMenu></leftMenu>
		</div>
		<div class="banner">
			<banner></banner>
		</div>
	</div>
	
</template>

<script setup>
	import leftMenu from '@/components/home/leftMenu'
	import banner from '@/components/home/banner'
</script>

<style lang="less" scoped>
	.nav{
		display: flex;
		justify-content: space-between;
		width:var(--content-width);
		margin: 0 auto;
		padding-top: 10px;
		.main{
		}
		
	}
</style>