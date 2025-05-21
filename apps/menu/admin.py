from django.contrib import admin

# Register your models.py here.
from .models import SubMenu , MainMenu

admin.site.register(SubMenu)
admin.site.register(MainMenu)