<template>
	<div class="comment">
		<div class="detail" v-for="(item,index) in commentData" :key="index">
			<div class=" clearfix">
				<div class="left fl">
					<div class="header-content">
						<img :src="'http://'+item.user_image_url" alt="" />
						<span class="nick-name">{{item.nickname}}</span>
					</div>
				</div>
				<div class="right fl">
					<div class="star">
						<img src="@/assets/images/goods/star.png" alt="" v-for="index in item.score"/>
						<img src="@/assets/images/goods/star1.png" alt="" v-for="index in 5-item.score"/>
					</div>
					<div class="text">
						{{item.content}}
					</div>
					<div class="time">
						{{item.create_time.replace("T"," ")}}
					</div>
				</div>
			</div>
			<hr />

		</div>
		<div v-if="commentCount===0" class="no-comment">
			评论空空如也
		</div>
		
		<div class="change-page">
			<div class="block">
				<el-pagination layout='prev , pager , next' 
				:total='commentCount'
				:page-size="15"
				@current-change="handleCurrentChange"
				></el-pagination>
			</div>
		</div>
	</div>
</template>


<script setup>
import { onMounted, ref } from 'vue';
import {getCommentCount,getCommentData} from '@/network/comment'
	
	let skuId = defineProps(['skuId'])
	let commentData = ref([])
	let commentCount = ref(0)
	onMounted(()=>{
		getCommentCount(skuId.skuId).then(res=>{
			commentCount.value = res.data
		})
		getCommentData(skuId.skuId,1).then(res=>{
			commentData.value = res.data
		})
	})
	
	const handleCurrentChange = (value)=>{
		console.log(value);
		getCommentData(skuId.skuId,value).then(res=>{
			commentData.value = []
			commentData.value = res.data
		})
	}
	
</script>

<style lang="less" scoped>
	.comment{
		.detail{
			margin: 10px;
			.left{
				.header-content{
					img{
						height: 25px;
						width: 25px;
						border-radius: 25px;
					}
					.nick-name{
						margin-left: 10px;
					}
				}
			}
			.right{
				width: 830px;
				margin-left:70px ;
				.star{
					img{
						height: 14px;
						height: 14px;
					}
				}
				.text{
					font-size: 14px;
					color: #333;
					margin-top: 10px;
				}
				.time{
					color: #999;
					margin-top: 10px;
				}
			}
			hr{
				margin-top: 10px;
				margin-bottom:10px ;
				border: 1px solid #ddd;
			}

		}
		.change-page{
			margin-top: 20px;
			margin-bottom: 20px;
			margin-left: 65%;
		}
		.no-comment{
			font-size:50px;
		}
	}
	
</style>