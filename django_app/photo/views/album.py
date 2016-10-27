from django.shortcuts import redirect, render, get_object_or_404
from ..models import Album

__all__ = [
    'album_list',
]

def album_list(request):
    albums = Album.objects.all()
    context = {
        'albums':albums,
    }
    return render(request, 'photo/album_list.html', context)