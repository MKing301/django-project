from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Post

# Create your views here.
def blog(request):
    posts = Post.objects.all()

    return render(request=request,
                  template_name='blog/home.html',
                  context={'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('blog:post_detail', slug=post.slug)

    else:
        form = CommentForm()

    return render(request=request,
                  template_name='blog/post_detail.html',
                  context={'post': post, 'form': form})