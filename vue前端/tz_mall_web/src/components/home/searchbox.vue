<template>
	<div class="main">
		<div class="content">
			<input type="text" placeholder="tz1344" ref='searchword' @keyup.enter="search($refs.searchword.value)" />
			<span class='iconfont icon-fangdajing' @click="search($refs.searchword.value)"></span>
		</div>
		<div class="hotword">
			<a v-for="(item,key) in hotwords"
			:key="key"
			:class = 'item.active===true?"active":""'
			@click='search(item.word)'
			>{{item.word}}</a>
		</div>
	</div>
</template>

<script setup>
import {onMounted, ref} from 'vue';
import { useRouter,useRoute} from 'vue-router';
const router = useRouter()
const route = useRoute()
	const hotwords = ref([
		{"word":"电脑","active":true},
		{"word":"手机","active":false},
		{"word":"平板","active":false},
	]);
	
	const search = (keyword)=>{
		console.log(keyword);
		if (!keyword){
			alert('nima')
			return
		}
		router.push('/goods_list/'+keyword+'/1/1')
		hotwords.value.forEach((d)=>{
			if(d.word == keyword){
				d.active=true
			}else{
				d.active=false
			}
		})

	}
	
	onMounted(()=>{
		let keyword = route.params.keyword
		if (!keyword){
			return 
		}
		hotwords.value.forEach((d)=>{
			if(d.word == keyword){
				d.active=true
			}else{
				d.active=false
			}
		})
	})
	
</script>

<style lang="less" scoped>
@red:#e2231a;
	.main{
		height:100px;
		margin-top: 45px;
	}

	.content{
		width:550px;
		height: 35px;
		border: 2px solid @red;
		display: flex;
		flex-direction: row;
		margin: auto auto;
		margin-left: 80px;
		// overflow: hidden;
	}
	input{
		flex: 1 0 460px;
		line-height: 35px;
		height: 35px;
		padding-left: 15px;
	}
	.iconfont{
		flex: 2 0 40px;
		line-height: 35px;
		height: 35px;
		// padding-left: 20px;
		text-indent:25px
	}
	span{
		background-color: #e2231a;
		cursor: pointer;
		color: white;
		font-weight: 700;
		&:hover{
			background-color: #c81623;
		}
	}
	.hotword{
		margin-left: 80px;
		margin-top: 10px;
		a{
			color: #999;
			margin-right: 10px;
			&:hover{
				color: #c81623;
				display: inline; /* 确保只对文字宽度应用 */
				border-bottom: 2px solid currentColor; /* 使用当前文字颜色 */
				padding-bottom: 2px; /* 可调整下划线与文字间距 */
			}
		}
	}
	.hotword .active{
		color: #e2231a ; 
	}

</style>