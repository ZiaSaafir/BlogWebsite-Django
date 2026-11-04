# [COPY & IMPLEMENT]
# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Post
from .forms import PostForm

def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted'),
        'title': 'Home Feed'
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def register(request):
    """
    Handles user account registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def post_create(request):
    """
    Creates a new post and automatically assigns the logged-in user as author.
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog-home')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_update(request, pk):
    """
    Updates an existing post ONLY if the logged-in user is the author.
    """
    post = get_object_or_404(Post, pk=pk)
    
    # AUTHORIZATION CHECK
    if post.author != request.user:
        return HttpResponseForbidden("You are not authorized to edit this post.")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    """
    Deletes a post ONLY if the logged-in user is the author.
    """
    post = get_object_or_404(Post, pk=pk)
    
    # AUTHORIZATION CHECK
    if post.author != request.user:
        return HttpResponseForbidden("You are not authorized to delete this post.")

    if request.method == 'POST':
        post.delete()
        return redirect('blog-home')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
