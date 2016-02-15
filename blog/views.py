# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, get_object_or_404
from models import BlogPost, Comment, Category
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm
from django.core.context_processors import csrf


def archive(request, page_number=1):
    posts = BlogPost.objects.all()
    current_page = Paginator(posts, 3, orphans=1)
    return render_to_response('blog/posts.html', {'posts': current_page.page(page_number),
                                                  'projects': Category.objects.all(),
                                                  'username': auth.get_user(request).username})


def article(request, slug):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['post'] = get_object_or_404(BlogPost, slug=slug)
    id_post = BlogPost.objects.get(slug=slug)
    args['comments'] = Comment.objects.filter(comments_blog_id=id_post.id)
    args['form'] = comment_form
    args['projects'] = Category.objects.all()
    args['username'] = auth.get_user(request).username
    return render_to_response('blog/post.html', args)


@ login_required()
def add_like(request, blog_id):
    try:
        if blog_id in request.COOKIES:
            return_path = request.META.get('HTTP_REFERER', '/')
            return redirect(return_path)
        else:
            blog_get = BlogPost.objects.get(id=blog_id)
            blog_get.likes += 1
            blog_get.save()
            return_path = request.META.get('HTTP_REFERER', '/')
            response = redirect(return_path)
            response.set_cookie(blog_id, 'like')
            return response
    except ObjectDoesNotExist:
        return redirect('/')


def add_comment(request, blog_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.comments_blog = BlogPost.objects.get(id=blog_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/')


def blog_cat(request, category_id=1):
    args = {'projects': Category.objects.all(),
            'category': Category.objects.get(id=category_id),
            'post': BlogPost.objects.filter(category_id=category_id)}
    branch_categories = args['category'].get_descendants(include_self=True)
    args['category_blog'] = BlogPost.objects.filter(category__in=branch_categories).distinct()
    return render_to_response('blog/blog_cat.html', args)
