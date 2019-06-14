# coding=utf-8
from django import forms
from blog_sys.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_user', 'content', 'comment_blog']


