<template>
	<div>
		<Shortcut></Shortcut>
		<Header></Header>
		<div class="inner">
			<navigation></navigation>
			<div class="findgoods">
				<FindGood></FindGood>
			</div>
			<div class="category">
				<div class="content" v-for="(item,index) in category" :key="index">
					<div class='items' :class='{active:item.selected}' @click="toCategory(item.typeId)">
						<div class="category-title">{{item.title}}</div>
						<div class="category-content">{{item.content}}</div>
					</div>
				</div>
			</div>
			<Category :categoryId='categoryId'></Category>
		</div>
		<el-backtop right="200" bottom="200"></el-backtop>
	</div>
	
</template>

<script setup>
import { ref ,onMounted} from 'vue'
import Shortcut from '@/components/common/Shortcut'
import Header from '@/components/home/Header'
import navigation from '@/components/home/Navigation'
import FindGood from '@/components/home/findgoods'
import Category from '@/components/home/Category'
import { useStore } from 'vuex'
	
	const store = useStore()

	let category = ref([
		{'typeId':1,'title':'精选','content':'猜你喜欢','selected':true},
		{'typeId':2,'title':'智能先锋','content':'大电器城','selected':false},
		{'typeId':3,'title':'居家优品','content':'品质生活','selected':false},
		{'typeId':4,'title':'超市百货','content':'百货生鲜','selected':false},
		{'typeId':5,'title':'时尚达人','content':'美妆穿搭','selected':false},
		{'typeId':6,'title':'进口好物','content':'京东国际','selected':false},
	])
	
	let categoryId = ref(1)
	const toCategory = function(typeId){
		categoryId.value = typeId
		for(let i in category.value){
			category.value[i].selected = false
			if (typeId-1 == i ){
				category.value[i].selected = true
			}
		}
	}
	
	onMounted(()=>{
		store.dispatch('updataCart')
	})
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
@red:#e2231a;
	.inner{
		background-color: #f4f4f4;
	}
	.inner .findgoods{
		padding-top: 25px;
		padding-bottom: 25px;
	}
	.inner .category {
		width: var(--content-width);
		margin: 0 auto;
		display: flex;
		flex-direction: row;
		background-color: white;
		justify-content: space-between;
		.content{
			height: 60px;
			text-align: center;
			justify-content: space-between;
			position: relative;
			width: 80px;
			&:not(:last-child):after{
				content: '';
				position: absolute;
				top: 50%;
				transform: translateY(-15px) ;
				left: 165%;
				height: 30px;
				border: 1px solid #e8e8e8 ;
			}
			&:last-child{
				margin-right: 100px;
			}
			&:first-child{
				margin-left: 100px;
			}
			.active .category-title{
				background-color: #e1251b;
				color: white;
				border-radius: 15px;
			}
			.items{
				line-height: 20px;
				text-align: center;
				margin-top: 10px;
				&:hover{
					cursor: pointer;
					color: @red ;
					.category-content{
						color: @red;
					}
				}
				.category-title{
					font-size: 16px;
					font-weight: 700px;
					line-height: 25px;
				}
				.category-content{
					font-size: 12px;
					color: #999;
				}	
			}

		}
	}
</style>
