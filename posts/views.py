from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from posts.forms import CommentForm, CreateTagForm, CreatePostForm
from posts.models import Post, Tag
from posts.utils import ObjectCreateMixin


class Index(View):
    def get(self, request):
        post_on_page = 10
        posts = Post.objects.all()
        tags = Tag.objects.annotate(posts_count=Count('posts')).order_by('-posts_count')
        paginator = Paginator(posts, post_on_page)
        page = request.GET.get('page')
        posts_10_on_page = paginator.get_page(page)

        return render(request, 'index.html', context={'posts_10_on_page': posts_10_on_page,
                                                      'tags': tags})


class PostDetails(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        comments = post.comments.all()
        comment_form = CommentForm()
        return render(request, 'post_details.html', context={'post': post,
                                                             'comments': comments,
                                                             'comment_form': comment_form})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        comments = post.comments.all()

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = CommentForm()

        return render(request, 'post_details.html', context={'post': post,
                                                             'comments': comments,
                                                             'comment_form': comment_form})


class CreatePost(ObjectCreateMixin, View):
    template = 'create_post.html'
    model_form = CreatePostForm


class CreateTag(ObjectCreateMixin, View):
    template = 'create_tag.html'
    model_form = CreateTagForm


class TagPosts(View):
    def get(self, request, slug):
        posts = Post.objects.filter(tags__slug=slug)
        return render(request, 'tags.html', context={'posts': posts,
                                                     'tag_slug': slug, })
