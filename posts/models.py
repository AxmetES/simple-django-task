from django.db import models
from django.db.models import Count
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args={'slug': self.slug})

    @property
    def get_commets_count(self):
        return f"комментариев: {Post.objects.filter(pk=self.pk).aggregate(Count('comments'))['comments__count']}"

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_filter', args={'tag_title': self.slug})

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'коммент'
        verbose_name_plural = 'комментарии'
