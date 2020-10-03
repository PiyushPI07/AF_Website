from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
# InstagramUserRecentMediaNode is a class in django_instagram 3rd party app responsible for getting instagram data. note that keywords 'context', 'profile' and 'recent_media' are specific to this 3rd party app. please refrain from renaming them.
from django_instagram.templatetags.instagram_client import InstagramUserRecentMediaNode
from .models import *


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


#filter for instagram posts
def post_filter(media, keyword):
    if media['edge_media_to_caption']['edges']:
        if keyword in media['edge_media_to_caption']['edges'][0]['node']['text']:
            return True
        else:
            return False
    else:
        return False

def udaan_view(request, *args, **kwargs):
    static_data= Udaan_static.objects.get(id=1)
    carousel_imgs = Udaan_image.objects.filter(display_on_caurosel = True)
    events = Udaan_event.objects.all()
    context = {
        'static': static_data,
        'carousel_images': carousel_imgs,
        'event_list': events,
        "profile": "afnitk",                                                                                                #instagram profile
        'recent_media': [],                                                                                                 #contains data of all recent instagram posts
        'filtered_posts':[]                                                                                                 #contains filtered instagraam posts
    }
    InstagramUserRecentMediaNode(context['profile']).render(context)                                                        #brings all recent instagram posts data to the context. 
    context['filtered_posts'] = list(filter(lambda x: post_filter(x, static_data.insta_keyword), context['recent_media']))  #filters the posts
    return render(request, 'udaan.html', context)

def contact(request):
    image_gallery_full = Image.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    context = {
        'image_gallery_full': image_gallery_full,
        'image_gallery_short': image_gallery_short,
    }
    return render(request, 'contact.html', context=context)
