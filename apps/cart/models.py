from django.db import models

# Create your models.py here.

class Cart(models.Model):
	id = models.AutoField(primary_key=True,null=False,unique=True,verbose_name='购物车id')
	sku_id = models.CharField(null=False,max_length=255,unique=True,verbose_name='物品id')
	nums = models.IntegerField(verbose_name='购物数量')
	email = models.CharField(max_length=255,verbose_name='用户邮箱')
	is_delete = models.BooleanField(default=False,verbose_name='是否删除')
	create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

	class Meta:
		db_table = 'shopping_cart'
		verbose_name = '购物车表'
		verbose_name_plural = verbose_name
