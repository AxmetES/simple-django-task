from django import forms

from posts.models import Comment, Post, Tag


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CreateTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'slug', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),

        }
