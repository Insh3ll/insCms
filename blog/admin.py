from django.contrib import admin
from blog.models import Category, Article

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name','desc')

class ArticAdmin(admin.ModelAdmin):
	list_display = ('title','author','published','pub_date','views')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticAdmin)