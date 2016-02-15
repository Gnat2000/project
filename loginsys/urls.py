from django.conf.urls import include, url
from django.contrib.auth.views import login, logout

urlpatterns = [
        url(r'^login/$', 'loginsys.views.login'),
        url(r'^logout/$', 'loginsys.views.logout'),
        url(r'^register/$', 'loginsys.views.register'),
]