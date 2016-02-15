from django.shortcuts import render_to_response, redirect
from models import Photo, Album
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist


def album(request):
    albums = Album.objects.all()
    return render_to_response('gallery/album.html', {'albums': albums,
                                                     'username': auth.get_user(request).username})


def photo(request, post_id):
    try:
        albums = Album.objects.get(biography_id=post_id)
        photos = Photo.objects.filter(blog_post_id=post_id)
        return render_to_response('gallery/photo.html', {'photos': photos, 'albums': albums,
                                                         'username': auth.get_user(request).username})
    except ObjectDoesNotExist:
        return_path = request.META.get('HTTP_REFERER', '/')
        return redirect(return_path)
