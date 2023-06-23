from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category


def index(request):
    template = 'blog/index.html'
    post_list = (
        Post.objects.select_related('category', 'location')
        .filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now()
        )[:5]
    )
    context = {'post_list': post_list}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True)
    post_list = (
        category.posts
        .filter(is_published=True, pub_date__lte=timezone.now())
    )
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template, context)


def post_detail(request, id):
    post = (
        get_object_or_404(
            Post.objects.select_related('category'),
            id=id,
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now()
        )
    )
    template = 'blog/detail.html'
    context = {'post': post}
    return render(request, template, context)
