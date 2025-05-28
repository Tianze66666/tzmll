<template>
	<div class='left-menu' @mouseleave="noItem()">
		<ul class="ulist">
			<li v-for='(item,index) in showMainData' 
			:key="index"
			@mouseenter="showItem(item.index)"
			>
				<span v-for='(d,i) in item.data' :key='i'>
					<a :href="'/goods_list/'+d.name+'/1/1'">{{d.name}}</a>
					<span v-if='item.data.length-i-1'>/</span>
				</span>
			</li>
<!-- 			<li>
				<span>
					<a href="#">手机</a>
					<span>/</span>
					<a href="#">运营商</a>
					<span>/</span>
					<a href="#">数码</a>
					<span>/</span>
				</span>
			</li> -->
		</ul>
		<div class="second-item" v-show='isShowItem'>
			<!-- showSecondMenuIndex -->
			<secondmenu :showSecondMenuIndex></secondmenu>
		</div>
	</div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue';
import { getMainMenu } from '@/network/home';
import logoVue from '../common/logo.vue';
import secondmenu from './secondmenu'
	let leftMenuData = ref([])
	onMounted(()=>{
		getMainMenu().then(res=>{
			init_menu_data(res.data)
		})
	})
	const init_menu_data = function(menuData){
		for(let i in menuData){
			// let jsonData = JSON.parse(menuData[i])
			let jsonData = menuData[i]
			leftMenuData.value.push(jsonData)
		}
	}
	
	// 接口返回的数据需要进行加工，基本结构为[{index:1,data:[]},]
	const showMainData = computed(()=>{
		let resultList = []
		let result = {'index':'',data:[]};
		for(let i in leftMenuData.value){
			let id = leftMenuData.value[i].main_menu_id;
			let data = {'name':leftMenuData.value[i].main_menu_name}
			if(result['index'] !== null && id == result['index']){
				result['data'].push(data)
			}else{
				result = {'index':'',data:[]}
				result['index'] = id
				result['data'].push(data)
				resultList.push(result)
			}
		}
		return resultList;
	})

	// 二级菜单显示与隐藏
	let isShowItem = ref(false)
	let showSecondMenuIndex = ref()
	const showItem = (index)=>{
		// 显示二级菜单
		isShowItem.value = true
		showSecondMenuIndex.value = index
	}
	const noItem = function(){
		// 隐藏二级菜单
		isShowItem.value = false
		
	}
	
	

</script>

<style lang="less" scoped>
@red:#e2231a;
	.left-menu{
		position: relative;
		background-color: #fff;
		height: 485px;
		width: 190px;
		ul{
			padding-top: 10px;
			li{
				padding-left: 15px;
				padding-top: 1px;
				// padding-bottom: 5px;
				line-height: 25px;
				height: 25px;
				&:hover{
					cursor: pointer;
					background-color: #d9d9d9;

				}
				
				a{
					font-size: 14px;
					color:#333;
					
					&:hover{
						cursor: pointer;
						color: @red;
					}
					
				}

			}
		}
	}
	.left-menu .second-item{
		position: absolute;
		top:0px;
		left: 100%;
		z-index: 999;
		overflow: hidden;
		transform: 1s;
	}

</style>