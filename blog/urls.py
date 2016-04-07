from django.conf.urls import url
from blog import views 

urlpatterns = [
	url(r'^$',views.index,name='home'),
	url(r'^category_detail/',views.category_detail,name='category_detail'),
	url(r'^article_detail/',views.article_detail,name='article_detail'),
]