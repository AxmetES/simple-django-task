from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect

from posts.forms import CommentForm
from posts.models import Post, Tag


def index(request):
    post_on_page = 10
    posts = Post.objects.all()
    tags = Tag.objects.annotate(posts_count=Count('posts')).order_by('-posts_count')
    paginator = Paginator(posts, post_on_page)
    page = request.GET.get('page')
    posts_10_on_page = paginator.get_page(page)

    return render(request, 'index.html', context={'posts_10_on_page': posts_10_on_page,
                                                  'tags': tags})


def post_details(request, slug):
    post = get_object_or_404(Post, slug__iexact=slug)
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'post_details.html', context={'post': post,
                                                         'comments': comments,
                                                         'comment_form': comment_form})


def tags(request, slug):
    posts = Post.objects.filter(tags__slug=slug)
    return render(request, 'tags.html', context={'posts': posts})
