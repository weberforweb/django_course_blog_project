from django import forms

from .models import BlogPost


class AddPost(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'author', 'status']
