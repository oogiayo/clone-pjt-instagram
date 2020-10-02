from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from .forms import PostForm


# Create your views here.
@login_required
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # post.photo = request.FILES['photo']
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)


@require_POST
def delete(request, post_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    post = get_object_or_404(Post, pk=post_pk)
    if post.user==request.user:
        post.delete()
        return redirect('posts:index')
    return redirect('posts:detail', post_pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('posts:detail', post_pk)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
    }
    return render(request, 'posts/update.html', context)
