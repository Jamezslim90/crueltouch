import random

from django.shortcuts import render, redirect
from portfolio.models import Photo, Album


def index_portfolio(request):
    all_photos = Photo.objects.all()
    all_albums = Album.objects.all()
    list_of_photo = list(all_photos)
    random.shuffle(list_of_photo)
    return render(request, 'portfolio/index_portfolio.html', {
        'all_photos': list_of_photo,
        'all_albums': all_albums,
    })

