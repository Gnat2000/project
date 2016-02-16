"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/addlike/(?P<blog_id>\d+)/$', 'blog.views.add_like'),
    url(r'^blog/addcomment/(?P<blog_id>\d+)/$', 'blog.views.add_comment'),
    url(r'^category/get/(?P<category_id>\d+)/$', 'blog.views.blog_cat'),
    url(r'^blog/(.*)/$', 'blog.views.article'),
    url(r'^blog/$', 'blog.views.archive'),
    url(r'^page/(\d+)/$', 'blog.views.archive'),
    url(r'^$', 'blog.views.archive'),
]
