from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Post
from .forms import PostForm

# function base views
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        
    # if request.method == 'POST':
    #     print request.POST.get('title')
    #     print request.POST.get('content')
    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)

def post_detail(request, id=None):
    post = get_object_or_404(Post, id=id)
    context = {
        'title': 'Detail',
        'post': post,
    }
    return render(request, 'posts/detail.html', context)

def post_list(request):
    posts = Post.objects.all()
    context = {
        'title': 'List',
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

def post_update(request):
    return HttpResponse('<h1>Update</h1>')

def post_delete(request):
    return HttpResponse('<h1>Delete</h1>')  