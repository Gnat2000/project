from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'gallery.views.album'),
    url(r'^(?P<post_id>\d+)/$', 'gallery.views.photo'),
]
