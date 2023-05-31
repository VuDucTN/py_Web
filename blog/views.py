from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Post
from .form import PostForm
from django.core.paginator import Paginator
# Create your views here.
def list(request):
    post = Post.objects.all().order_by('-date')

    paginator = Paginator(post, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', {'page_obj' : page_obj})

def post(request, id):
    post = Post.objects.get(id = id)
    return render(request, 'blog/post.html', {'post': post})
def create_view(request):
    if request.method == 'POST':
        post = Post()
        post.title = request.POST.get('title')
        post.description = request.POST.get('description')
        post.body = request.POST.get('body')
 
        if len(request.FILES) != 0:
            post.image = request.FILES['image']

        post.save()
        return redirect('/blog/')
    return render(request, 'blog/create_view.html')
def success(request):
    return HttpResponse('successfully uploaded')
def search(request):
    query = request.GET['query']
    Posts = Post.objects.filter(title__icontains=query)
    paginator = Paginator(Posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', {'page_obj' : page_obj})

