#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class Category(models.Model):
	name = models.CharField('分类名称',max_length=256)
	desc = models.CharField('分类描述',max_length=512)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = '分类'
		verbose_name_plural = '分类'

class Article(models.Model):
	category = models.ManyToManyField(Category,verbose_name='分类')

	title = models.CharField('标题',max_length=256)
	author = models.ForeignKey('auth.User',blank=True,null=True,verbose_name='作者')
	pub_date = models.DateTimeField('发布时间',auto_now_add=True,editable=True)
	mod_date = models.DateTimeField('更新时间',auto_now=True,null=True)
	content = UEditorField('内容', height=300, width=1000,
        		default=u'', blank=True, imagePath="uploads/images/",
        		toolbars='besttome', filePath='uploads/files/')
	views = models.IntegerField('阅读次数',default=1)

	published = models.BooleanField('正式发布',default=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = '文章'
		verbose_name_plural = '文章'
