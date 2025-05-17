import json

from django.db import models

# Create your models.py here.

from django.db import models


class SubMenu(models.Model):
    main_menu_id = models.IntegerField(blank=True, null=True)
    sub_menu_id = models.IntegerField(blank=True, null=True)
    sub_menu_type = models.CharField(max_length=255, blank=True, null=True)
    sub_menu_name = models.CharField(max_length=255, blank=True, null=True)
    sub_menu_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_menu'
        verbose_name = '子菜单表'
        verbose_name_plural = verbose_name

    def __str__(self):
        result = {}
        result['main_menu_id'] = self.main_menu_id
        result['sub_menu_id'] = self.sub_menu_id
        result['sub_menu_type'] = self.sub_menu_type
        result['sub_menu_name'] = self.sub_menu_name
        return result


class MainMenu(models.Model):
    main_menu_id = models.IntegerField()
    main_menu_name = models.CharField(max_length=255)
    main_menu_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_menu'
        verbose_name = '主菜单表'
        verbose_name_plural = verbose_name

    def __str__(self):
        result = {}
        result['main_menu_id'] = self.main_menu_id
        result['main_menu_name'] = self.main_menu_name
        # result['main_menu_url'] = self.main_menu_url
        return str(result)