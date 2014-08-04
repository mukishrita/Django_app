# Create your views here.

from blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
from .forms import PostForm

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def post_new(request):
	form = PostForm()
	return render_to_response('post_edit.html', {'form': form})

def post_list(request):
	pass