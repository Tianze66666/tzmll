from django.db import models

# Create your models here.

class Cart(models.Model):
	id = models.AutoField(primary_key=True,null=False,unique=True,verbose_name='购物车id')
	sku_id = models.CharField(null=False,max_length=255,unique=True,verbose_name='物品id')
	nums = models.IntegerField(verbose_name='购物数量')
	is_delete = models.BooleanField(default=False,verbose_name='是否删除')

	class Meta:
		db_table = 'shopping_cart'
		verbose_name = '购物车表'
		verbose_name_plural = verbose_name
