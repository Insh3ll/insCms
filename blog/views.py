from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Category, Article

# Create your views here.
def index(request):
	categorys = Category.objects.all()
	articles = Article.objects.all().filter(published=True).order_by('-id')
	paginator = Paginator(articles,5)
	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	ctx = {
		'categorys': categorys,
		'articles': articles,
	}

	return render(request,'blog/index.html',ctx)

def category_detail(request):
	categ_id = request.GET.get('id',1)
	category = Category.objects.get(pk=categ_id)
	articles = Article.objects.filter(category=category,published=True).order_by('-id')
	paginator = Paginator(articles,3)
	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	ctx = {
		'category': category,
		'articles': articles,
	}

	return render(request,'blog/category_detail.html',ctx)

def article_detail(request):
	article_id = request.GET.get('id',1)
	article = Article.objects.get(pk=article_id)
	article.views += 1
	article.save()
	ctx = {
		'article': article,
	}

	return render(request,'blog/article_detail.html',ctx)