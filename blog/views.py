from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def home(request):
    query = request.GET.get('q')

    posts_list = Post.objects.all().order_by('-id')

    if query:
        posts_list = posts_list.filter(title__icontains=query)

    paginator = Paginator(posts_list, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'blog/home.html', {
        'posts': posts,
        'query': query
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {
        'post': post
    })
