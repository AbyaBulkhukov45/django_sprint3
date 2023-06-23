from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category

POSTS_LIMIT = 5


def get_published_posts():
    return Post.objects.select_related('category', 'location').filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    template = 'blog/index.html'
    post_list = get_published_posts()[:POSTS_LIMIT]
    context = {'post_list': post_list}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True
                                 )
    post_list = get_published_posts().filter(category=category)
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    post = get_object_or_404(get_published_posts(), id=id)
    template = 'blog/detail.html'
    context = {'post': post}
    return render(request, template, context)
