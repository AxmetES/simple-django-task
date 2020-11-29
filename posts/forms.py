from django import forms

from posts.models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }

