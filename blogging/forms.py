from django import forms
from blogging.models import Post


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("title", "text")
