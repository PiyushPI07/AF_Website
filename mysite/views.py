from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from account.forms import VolunteerForm, SandArtRegistrationForm
from django.views.decorators.cache import cache_control
from django.shortcuts import get_object_or_404, render

from .models import *


def index(request):
    full_member_list = Member.objects.all()
    art_list = Art.objects.all()
    art_image = ArtImage.objects.all()
    event_list = []
    context = {
        'full_member_list': full_member_list,
        'art_list': art_list,
        'event_list': event_list,
        'image_gallery_short': image_gallery_short,
        'render_recruitment_form': True,
        'art_image': art_image,
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


# def udaan(request):
#     full_member_list = Member.objects.all()
#     image_gallery_full = Image.objects.all()
#     art_list = Art.objects.all()
#     blog_list = Blog.objects.all()
#     event_list = Event.objects.all()
#     image_gallery_short = Image.objects.filter(display_on_index=True)
#     context = {
#         'full_member_list': full_member_list,
#         'image_gallery_full': image_gallery_full,
#         'art_list': art_list,
#         'blog_list': blog_list,
#         'event_list': event_list,
#         'image_gallery_short': image_gallery_short
#     }
#     return render(request, 'udaan.html', context=context)

def udaan_view(request, *args, **kwargs):
    static_data= Udaan_static.objects.get(id=1)
    carousel_imgs = Udaan_image.objects.filter(display_on_caurosel = True)
    events = Udaan_event.objects.all()
    context = {
        'static': static_data,
        'carousel_images': carousel_imgs,
        'event_list': events,
        'is_form_submitted': False,
    }
def events(request):
    event_list = Event.objects.all()
    event_image = EventImage.objects.all()
    context = {
        'event_list': event_list,
        'event_image': event_image
    }
    return render(request, 'events.html', context=context)

    if request.POST:
        form = SandArtRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thank_you')
        else:
            context['form'] = form
    else:
        form = SandArtRegistrationForm()
        context['form'] = form
    return render(request, 'udaan.html', context)

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
    return render(request, 'contact.html', context=context)
def thank_you(request):
    return render(request, 'thank_you.html', context={})

    return render(request, 'gallery.html', context= context)


def contact(request):
    return render(request, 'contact.html')
