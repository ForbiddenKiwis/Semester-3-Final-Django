from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all()
    extra_property = "Latest Posts"
    return render(request, 'posts/index.html', {'posts': posts, 'extra_property': extra_property})

def details(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    context = {'post': post}

    return render(request, 'posts/details.html', context)

# Create your views here.
