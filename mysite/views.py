from django.shortcuts import render
from .models import *
from django.conf import settings


def index(request):
    full_member_list = Member.objects.all()
    image_gallery_full = Image.objects.all()
    blog_list = Blog.objects.all()
    event_list = Event.objects.all()
    art_list = Art.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    context = {
        'full_member_list': full_member_list,
        'image_gallery_full': image_gallery_full,
        'blog_list': blog_list,
        'art_list': art_list,
        'event_list': event_list,
        'image_gallery_short': image_gallery_short
    }
    return render(request, 'index.html', context=context)


def about(request):
    full_member_list = Member.objects.all()
    image_gallery_full = Image.objects.all()
    blog_list = Blog.objects.all()
    event_list = Event.objects.all()
    art_list = Art.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    context = {
        'full_member_list': full_member_list,
        'image_gallery_full': image_gallery_full,
        'art_list': art_list,
        'blog_list': blog_list,
        'event_list': event_list,
        'image_gallery_short': image_gallery_short
    }
    return render(request, 'about.html', context=context)


def blog(request):
    full_member_list = Member.objects.all()
    image_gallery_full = Image.objects.all()
    blog_list = Blog.objects.all()
    event_list = Event.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    context = {
        'full_member_list': full_member_list,
        'image_gallery_full': image_gallery_full,

        'blog_list': blog_list,
        'event_list': event_list,
        'image_gallery_short': image_gallery_short
    }
    return render(request, 'blog.html', context=context)


# Create your views here.

def blog_details(request):
    full_member_list = Member.objects.all()
    image_gallery_full = Image.objects.all()
    blog_list = Blog.objects.all()
    event_list = Event.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    context = {
        'full_member_list': full_member_list,
        'image_gallery_full': image_gallery_full,
        'blog_list': blog_list,
        'event_list': event_list,
        'image_gallery_short': image_gallery_short
    }
    return render(request, 'blog_details.html', context=context)


def udaan(request):
    full_member_list = Member.objects.all()
    image_gallery_full = Image.objects.all()
    art_list = Art.objects.all()
    blog_list = Blog.objects.all()
    event_list = Event.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    context = {
        'full_member_list': full_member_list,
        'image_gallery_full': image_gallery_full,
        'art_list': art_list,
        'blog_list': blog_list,
        'event_list': event_list,
        'image_gallery_short': image_gallery_short
    }
    return render(request, 'udaan.html', context=context)


def contact(request):
    image_gallery_full = Image.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    context = {
        'image_gallery_full': image_gallery_full,
        'image_gallery_short': image_gallery_short,
    }
    return render(request, 'contact.html', context=context)
