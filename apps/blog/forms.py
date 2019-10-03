from django import forms

from .models import BlogPost


class BlogPostForm(forms.Form):
    slug = forms.SlugField()
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'is_published']
