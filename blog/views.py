from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-created_at') 
     # Fetch all posts from the database
    context = {
        'posts': posts  # Pass the posts to the template context
    }

    return render(request, 'blog/home.html', context)  # Render the 'home.html' template with the context data

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Fetch the post with the given primary key (pk)
    context = {
        'post': post  # Pass the post to the template context
    }   
    return render(request, 'blog/post_detail.html', context)  # Render the 'post_detail.html' template with the context data