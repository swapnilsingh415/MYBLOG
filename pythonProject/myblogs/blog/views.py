from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post

# Create your views here.
def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
    print(posts)
    data={
        'posts': posts
    }
    return render(request,'home.html',data)
def post(request, url):
    post = Post.objects.get(url=url)
    print(post)
    return render(request,'posts.html',{})