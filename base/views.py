from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import CommentForm


def index(request):
    posts = Post.objects.filter(status='publish').order_by('-publish')

    posts = posts.select_related('user').filter(publish__lte=timezone.now())

    context = {
        'posts': posts
    }

    return render(request, "base/index.html", context)


def single(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='publish', publish__lte=timezone.now())
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.instance.post_id = post_id

        if form.is_valid():
            form.save()
            return redirect('base:single', post_id=post_id)

    context = {
        'post': post,
        'form': form
    }

    return render(request, "base/single.html", context)
