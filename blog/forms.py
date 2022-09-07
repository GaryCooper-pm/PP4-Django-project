from .models import Comment
from django import forms

"""
Thanks to Code Institutes 'I Think Therefore I Blog'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/Django3blog
"""

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
