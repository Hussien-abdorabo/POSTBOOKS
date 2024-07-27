from django import forms
from .models import Post , Comment


class PostForm (forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":4}))
    
    class Meta:
        model = Post
        fields = ("title","content")


class PostupdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields =["title","content"]


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder" :"Add comment here"}))
    
    class Meta:
        model = Comment
        fields = ('content',)