from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from blogs.models import Blog, Category
from django.db.models import Q

# Create your views here.
##########################################################################################################################
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Publish', category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    
    context = {
        'posts': posts,
        'category': category,
    }
    
    return render(request, 'posts_by_category.html', context)

##########################################################################################################################
def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug)
    context = {
        'single_blog': single_blog,
    }
    
    return render(request, 'blogs.html', context)

##########################################################################################################################
def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword)) 
    context = {
        'blogs': blogs,
        'keyword': keyword
    }
    
    return render(request, 'search.html', context)