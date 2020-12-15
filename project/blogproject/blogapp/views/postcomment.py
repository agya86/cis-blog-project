from django.shortcuts import render, redirect
from ..forms import CommentForm
from ..models.blogcomment import Comment
from ..models.blogpost import Post
from django.contrib import messages


def Commentpage(request,id=0):
    blog=Post.objects.get(id=id)
    postid=id
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid :
            form.save()
            return redirect('homepage')
    else:    
        form=CommentForm()
        return render(request,'blog/commentform.html',{'form':form,'blog':blog,'postid':postid})