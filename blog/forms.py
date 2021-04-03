from django import forms
from .models import Post, Comment
from .widgets import CustomClearableFileInput


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'image',)
    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
