from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm , PostupdateForm , CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    posts = Post.objects.all()
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
           instance = form.save(commit=False)
           instance.author = request.user
           instance.save()
           return redirect("blog-index")
        
    else:
        form = PostForm()
  
    return render(request , "blogs/index.html" ,{
        "posts": posts,
        "form" : form
    })    



@login_required
def post_detail(request,id):
    post = Post.objects.get( pk = id)
    if request.method == "POST":
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit = False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('blog-post-detail', id=post.id)
    else:
        c_form = CommentForm()    
    return render(request, "blogs/post_detail.html",{
        "post" : post,
        "c_form" : c_form
    })



@login_required
def post_edit(request,id):
    post = Post.objects.get( pk = id)
    if request.method == "POST":
        form = PostupdateForm(request.POST, instance= post)
        if form.is_valid():
            form.save()
            return redirect("blog-post-detail", id =post.id)
    else:
        form = PostupdateForm(instance=post)    
    return render(request, "blogs/post_edit.html",{
        "post" : post,
        "form" : form
    })


@login_required
def post_delete(request,id):
    post = Post.objects.get( pk = id)
    if request.method =="POST":
        post.delete()
        return redirect("blog-index")
    
    return render(request, "blogs/post_delete.html",{
        "post" : post
    })
