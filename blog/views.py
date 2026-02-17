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


from .forms import CommentForm
from django.shortcuts import redirect

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.user = request.user
                comment.save()
                return redirect('blog:post_detail', slug=post.slug)
        else:
            return redirect('login')

    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form
    }

    return render(request, 'blog/post_detail.html', context)

