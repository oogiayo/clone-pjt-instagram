from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Tag
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from .forms import PostForm, CommentForm, TagForm

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
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            content = post.content.split()
            post.user = request.user
            post.save()

            content_new = ''
            for word in content:
                if word[0]=='#':
                    if {'content': word} in Tag.objects.all().values('content'):
                        tag = Tag.objects.get(content=word)
                        post.hashtags.add(tag)                
                    else:
                        tag = Tag.objects.create(content=word)
                        post.hashtags.add(tag)                
                else:
                    content_new += word
            post.content = content_new
            post.save()

            return redirect('posts:detail', post.pk)
    else:
        post_form = PostForm()
    context = {
        'post_form': post_form,
    }
    return render(request, 'posts/create.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comments = post.comment_set.all()
    form = CommentForm()
    content = post.content.split()
    context = {
        'form': form,
        'post': post,
        'comments': comments,
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


# Comments -----------------------------------------
@require_POST
def create_comment(request, post_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    post = get_object_or_404(Post, pk=post_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
    return redirect('posts:detail', post_pk)


@require_POST
def delete_comment(request, post_pk, comment_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    post = get_object_or_404(Post, pk=post_pk)
    comment = post.comment_set.get(pk=comment_pk)
    comment.delete()
    return redirect('posts:detail', post_pk)


# Like ---------------------------------
@require_POST
def like(request, post_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    post = get_object_or_404(Post, pk=post_pk)
    if post.like_users.filter(username=request.user).exists():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('posts:detail', post_pk)
