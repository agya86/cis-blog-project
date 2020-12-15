from django.shortcuts import render, redirect
from ..forms import PostForm
from ..models.blogpost import Post
from django.contrib import messages
# function Insert display and update operation on Post table
def Postpage(request,id=0):
    if request.user.is_authenticated:
        postlist=Post.objects.all().order_by('-created_on')
        if request.method=='GET':
            if id==0:
                postval=PostForm()
            else:
                postedit=Post.objects.get(pk=id)
                postval=PostForm(instance=postedit)
                

            return render(request, 'blog/postadd.html',{'post':postlist,'form':postval,'name': request.user})
        else:
            if  id==0:
                postval=PostForm(request.POST)
                msg="Insert Successfully"
            else:
                postedit=Post.objects.get(pk=id)
                postval=PostForm(request.POST,instance=postedit)
                msg="Update Successfully"
            if postval.is_valid:
                postval.save()
                messages.success(request,msg)
            return redirect('dashpage')
    else:
        return redirect('loginpage')

# delete operaion on post table  
def PostDelPage(request,id):
    postval=Post.objects.get(id=id)
    postval.delete()
    return redirect('dashpage')