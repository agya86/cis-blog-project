from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models.blogpost import Post
from .models.blogcomment import Comment
#User signup form
class RegisterForm(UserCreationForm):
    mobile=forms.CharField()
    address=forms.CharField()
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email' ) 

#comment insertion form
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('blogcomment','created_by','blog')
        widgets={
                        'blogcomment':forms.Textarea(attrs={'class':'form-control'}),
            'created_by':forms.TextInput(attrs={'class':'form-control'}),
        }

# post creation form
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','content','author')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'})
        }