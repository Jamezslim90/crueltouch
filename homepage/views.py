import random

from appointment.models import Service
from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views import generic

from crueltouch import settings
from .models import Photo


def index(request):
    try:
        album1 = Photo.objects.filter(album_id=1)
        album2 = Photo.objects.filter(album_id=2)
    except Photo.DoesNotExist:
        album1 = []
        album2 = []

    if album1 != [] or album2 != []:
        change_file_format(album1)
        change_file_format(album2)
        list_of_album1 = list(album1)
        list_of_album2 = list(album2)
        random.shuffle(list_of_album1)
        random.shuffle(list_of_album2)
    else:
        list_of_album1 = []
        list_of_album2 = []

    context = {
        'album1': list_of_album1,
        'album2': list_of_album2
    }
    return render(request, 'homepage/index.html', context)


def change_file_format(list_of_photo: list[Photo]):
    for photo in list_of_photo:
        photo.change_file_format()


class AboutView(generic.ListView):
    template_name = 'homepage/index_about_me.html'

    def get_queryset(self):
        return Photo.objects.all()


def get_logo(request):
    try:
        with open(settings.BASE_DIR / 'static/homepage/img/logos/logo.webp', 'rb') as f:
            return HttpResponse(f.read(), content_type="image/webp")
    except IOError:
        raise Http404("Image not found")


def get_logo_mini(request):
    try:
        with open(settings.BASE_DIR / 'static/homepage/img/logos/logo-mini.webp', 'rb') as f:
            return HttpResponse(f.read(), content_type="image/webp")
    except IOError:
        raise Http404("Image not found")


def promotions(request):
    return render(request, 'client/booking_and_promotions/promotions.html')


def get_robot_txt(request):
    try:
        with open(settings.BASE_DIR / 'static/homepage/robots.txt', 'rb') as f:
            return HttpResponse(f.read(), content_type="text/plain")
    except IOError:
        raise Http404("File not found")


def services_offered(request):
    page_title = _("Services | Maxify")
    page_description = _("Services offered by Maxify Global")
    all_services = Service.objects.all()
    # mobile_services = all_services.filter(name__icontains='Website')
    # web_services = all_services.filter(name__contains='Website')
    # # rest of category that isn't wedding and portrait
    # saas_services = all_services.filter(name__icontains='SaaS')
    # mvp_services = all_services.filter(name__icontains='MVP')
    context = {
        'page_title': page_title,
        'page_description': page_description,
        # 'mobile_services': mobile_services,
        # 'web_services': web_services,
        # 'saas_services': saas_services,
        # 'mvp_services': mvp_services,
        "all_services": all_services
    }
    return render(request, 'homepage/services_offered.html', context=context)
