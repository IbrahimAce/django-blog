from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

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



def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # redirect to homepage after saving
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})
