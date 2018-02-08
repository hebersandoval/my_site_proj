from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from .models import Post
from .forms import PostForm
from django.contrib import messages

# function base views
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        messages.success(request, 'Successfully created!')
        return HttpResponseRedirect(post.get_absolute_url())
    else:
        messages.error(request, 'Could not create your post!')
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

def post_update(request, id=None):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
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

def post_delete(request, id=None):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, 'Successfully deleted!')
    return redirect('posts:list')