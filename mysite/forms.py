from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('post', 'author', 'body', 'email')
        widgets = {
            'post' : forms.HiddenInput()
        }

