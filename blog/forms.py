from django import forms
from .models import Comment, Post, Category


# choices = [('Solo Rides', 'Solo Rides'), ('Group Rides', 'Group Rides')]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'category')

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'slug': forms.TextInput(attrs={'class': 'form-control'}),
        'author': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        'category': forms.Select(attrs={'class': 'form-control'}),
    }


"""
Thanks to Code Institutes 'I Think Therefore I Blog'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/Django3blog
"""


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
