from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from .models import Post
from .forms import PostForm

# function base views
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        messages.success(request, 'Successfully created!')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)

def post_detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'title': 'Detail',
        'post': post,
    }
    return render(request, 'posts/detail.html', context)

def post_list(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 3) # show 3 posts per page
    page_request_var = 'pagina'
    page = request.GET.get(page_request_var)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range (e.g. 9999), deliver last page of results
        posts = paginator.page(paginator.num_pages)
    context = {
        'title': 'List',
        'posts': posts,
        'page_request_var': page_request_var
    }
    return render(request, 'posts/index.html', context)

def post_update(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        messages.success(request, 'Successfully updated!')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'title': 'Update',
        'post': post,
        'form': form,
    }
    return render(request, 'posts/form.html', context)

def post_delete(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Successfully deleted!')
    return redirect('posts:list')