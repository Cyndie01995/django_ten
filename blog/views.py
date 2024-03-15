from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Post

# Create your views here.
# def index(request):
#     return HttpResponse("I love Django")
# def index(request):
#     all_posts = Post.objects.all()
#     con = {
#         'all_posts': all_posts
#     }
#     return render(request, 'blog/team.html', con)

# def index(request, id):
#     all_posts = Post.objects.get(id=id)
#     con = {
#         'all_posts': all_posts
#     }
#     return render(request, 'blog/team.html', con)

def post_list(request):
    posts = get_list_or_404(Post)
    return render(request, 'blog/team.html', {'posts': posts})

def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/team2.html', {'post': post})
