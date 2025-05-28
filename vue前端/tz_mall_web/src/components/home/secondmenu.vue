<template>
	<div class="second">
		<!-- 二级菜单..............{{showSecondMenuIndex}} -->
		<div class="menu-content" v-for="(item,index) in showSubMenuData" :key="index">

			<div class="menu-title">
				<span v-for="(d,i) in item.data" :key="i">
					<a :href="'/goods_list/'+d.name+'/1/1'" v-show="d.type==='channel'">
					{{d.name}}
					<img src="@/assets/images/menu/arrows-white.png" alt="" />
					</a>
				</span>
			</div>
			
			<div class="menu-detail">
				<div class="menu-detail-item">
					<span v-for="(d,i) in item.data" :key="i">
						<span class="menu-detail-tit" v-if='d.type==="dt"'>
							<a :href="'/goods_list/'+d.name+'/1/1'">
								{{d.name}}
							<img src="@/assets/images/menu/arrows-black.png" alt="" />
							</a>
						</span>
						<span class="menu-detail-data" v-else-if="d.type==='dd'">
							<a :href="'/goods_list/'+d.name+'/1/1'">{{d.name}}</a>
						</span>
					</span>
				</div>
			</div>
			
		</div>
	</div>
</template>

<script setup>
import { watch , ref, computed } from 'vue';
import { getSecondMenu } from '@/network/home'
	const showSecondMenuIndex=defineProps(['showSecondMenuIndex'])
	watch(showSecondMenuIndex,(newValue,oldValue)=>{
		// console.log(newValue.showSecondMenuIndex)
		getSecondMenu(newValue.showSecondMenuIndex).then((res)=>{
			// console.log(res.data);
			initMenuData(res.data)
		})
	})
	let subMenuData = ref([])
	const initMenuData = function(menuData){
		// 每次都要设置为空
		subMenuData.value = []
		for (let i in menuData){
			// let jsonData = JSON.parse(menuData[i])
			subMenuData.value.push(menuData[i])
		}
	}
	
	const showSubMenuData = computed(()=>{
		let resultList = [];
		let result = {'index':'','data':[]}
		for (let i in subMenuData.value){
			let id = subMenuData.value[i].sub_menu_id
			let data = {
				'name':subMenuData.value[i].sub_menu_name,
				'type':subMenuData.value[i].sub_menu_type,
			}
			if (result['index'] !== null && id == result['index']){
				result['data'].push(data)
			}else{
				result = {'index':'','data':[]}
				result['index'] = id
				result['data'].push(data)
				resultList.push(result)
			}
		}
		return resultList;
		
	})
		
	
	
	
</script>

<style lang="less" scoped>
@red:#e2231a;
	.second{
		width: 1000px;
		height: 445px;
		background-color: #fff;
		border: 2px solid #e9e9e9;
		padding: 20px;
		opacity: 0.95;
	}
		
	.second .menu-content{
		.menu-title{
			a{
				display: inline-block;
				background-color: black;
				height: 25px;
				color: white;
				margin-right: 10px;
				line-height: 25px;
				padding: 0 10px;
				font-weight: 500;
				&:hover{
					background-color: @red;
				}
				img{
					height: 18px;
				}
			}

		}
		
		.menu-detail{
			margin-top: 15px;
			.menu-datail-item{
				
			}
			.menu-detail-tit{
				a{
					font-weight: bold;
					&:hover{
						color: @red;
					}
					img{
						height: 18px;
					}
				}
			}
			.menu-detail-data{
				a{
					margin-left: 20px;
					&:hover{
						color:@red
					}
				}
			}
		}
	}
</style>