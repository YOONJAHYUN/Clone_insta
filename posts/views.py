from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            return redirect('posts:index')
    else:
        form = PostForm()

    context = {'form':form}
    return render(request, 'posts/create.html', context) 


def detail(request, post_pk):
    form = Post.objects.get(pk=post_pk)
    context = {
        'form':form
    }
    return render(request, 'posts/post.html', context)


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        post.delete()
        return redirect('posts:index')
    return redirect('posts:detail', post.pk)