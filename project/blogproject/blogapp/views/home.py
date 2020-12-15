from django.shortcuts import render, redirect
from ..models.blogpost import Post
from ..models.blogcomment import Comment
from django.http import JsonResponse
# display of post on home page
def Homepage(request):
    postlist=Post.objects.all().order_by('-created_on')
    commentlist=Comment.objects.all()
    return render(request,'blog/home.html',{'val':postlist,'commentval':commentlist})


# like conter for post
def LikePage(reqest,id):
    x=Post.objects.get(id=id)
    x.title=x.title
    x.content=x.content
    x.author=x.author
    x.updated_on=x.updated_on
    x.created_on=x.created_on
    x.likes=x.likes+1
    x.save()
    
    
    data = {
            'x': x.likes,
            
        }

    return JsonResponse(data)
    
