from django.conf import settings
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


def index(request):
    full_member_list = Member.objects.all()
    blog_list = Blog.objects.all()
    event_list = Event.objects.all()
    art_list = Art.objects.all()
    art_images = ArtImage.objects.all()

    context = {
        'full_member_list': full_member_list,
        'blog_list': blog_list,
        'art_list': art_list,
        'event_list': event_list,
        'art_images': art_images
    }
    return render(request, 'index.html', context=context)


def about(request):
    full_member_list = Member.objects.all()
    blog_list = Blog.objects.all()
    event_list = Event.objects.all()
    context = {
        'full_member_list': full_member_list,
        'blog_list': blog_list,
        'event_list': event_list
    }
    return render(request, 'about.html', context=context)


def blog(request):
    full_member_list = Member.objects.all()
    blog_list = Blog.objects.all()
    event_list = Event.objects.all()
    context = {
        'full_member_list': full_member_list,
        'blog_list': blog_list,
        'event_list': event_list
    }
    return render(request, 'blog.html', context=context)


def blog_post(request):
    full_member_list = Member.objects.all()
    blog_list = Blog.objects.objects.get(id)
    event_list = Event.objects.all()
    context = {
        'full_member_list': full_member_list,
        'blog_list': blog_list,
        'event_list': event_list,
        'image_gallery_short': image_gallery_short
    }
    return render(request, 'blog_post.html', context=context)


def events(request):
    event_list = Event.objects.all()
    event_img = EventImage.objects.all()
    context = {
        'event_list': event_list,
        'event_img': event_img
    }
    return render(request, 'events.html', context=context)


def udaan(request):
    full_member_list = Member.objects.all()
    blog_list = Blog.objects.all()
    event_list = Event.objects.all()
    context = {
        'full_member_list': full_member_list,
        'blog_list': blog_list,
        'event_list': event_list
    }
    return render(request, 'udaan.html', context=context)


def gallery(request):
    art_images = ArtImage.objects.all()
    gallery_img = Gallery.objects.all()
    event_images = EventImage.objects.all()
    context = {
        'gallery_img': gallery_img,
        'art_img': art_images,
        'event_img': event_images
    }
    return render(request, 'gallery.html', context= context)


def contact(request):
    full_member_list = Member.objects.all()
    gallery_img = Gallery.objects.all()
    context = {
        'full_member_list': full_member_list,
        'gallery_img': gallery_img
    }
    return render(request, 'contact.html', context=context)
