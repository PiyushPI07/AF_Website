from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import *


def index(request):
    full_member_list = Member.objects.all()
    art_list = Art.objects.all()
    art_image = ArtImage.objects.all()

    context = {
        'full_member_list': full_member_list,
        'art_list': art_list,
        'art_image': art_image
    }
    return render(request, 'index.html', context=context)


def about(request):
    full_member_list = Member.objects.all()
    context = {
        'full_member_list': full_member_list
    }
    return render(request, 'about.html', context=context)


def blog(request):
    blog_list = Blog.objects.all()
    context = {
        'blog_list': blog_list
    }
    return render(request, 'blog.html', context=context)


def blog_post(request,pk):
    blog_list = Blog.objects.filter(id=pk)
    context = {
        'blog_list': blog_list,
    }
    return render(request, 'blog_post.html', context=context)


def events(request):
    event_list = Event.objects.all()
    event_image = EventImage.objects.all()
    context = {
        'event_list': event_list,
        'event_image': event_image
    }
    return render(request, 'events.html', context=context)


def udaan(request):
    return render(request, 'udaan.html')


def gallery(request):
    art_image = ArtImage.objects.all()
    gallery_image = Gallery.objects.all()
    event_image = EventImage.objects.all()
    context = {
        'gallery_image': gallery_image,
        'art_image': art_image,
        'event_image': event_image
    }
    return render(request, 'gallery.html', context= context)


def contact(request):
    return render(request, 'contact.html')
