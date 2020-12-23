from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from account.forms import VolunteerForm, SandArtRegistrationForm
from django.views.decorators.cache import cache_control
from django.shortcuts import get_object_or_404, render
from .forms import CommentForm
from .models import *


def index(request):
    full_member_list = Member.objects.all()
    art_list = Art.objects.all()
    # art_image = ArtImage.objects.all()
    image_gallery_short = ''
    event_list = []
    context = {
        'full_member_list': full_member_list,
        'art_list': art_list,
        'event_list': event_list,
        'image_gallery_short': image_gallery_short,
        'render_recruitment_form': True,
        # 'art_image': art_image,
    }
    return render(request, 'index.html', context=context)


def about(request):
    year = datetime.datetime.now().year
    batches_to_display = [year-1, year-2, year-3, year-4]
    testimonials = Member.objects.filter(batch__in=batches_to_display).exclude(testimonial=None)
    context = {
        'testimonials': testimonials,
    }
    return render(request, 'about.html', context=context)


def blog(request):
    blog_list = Blog.objects.all()
    context = {
        'blog_list': blog_list
    }
    return render(request, 'blog.html', context=context)


def blog_post(request,pk):
    blog = Blog.objects.get(id=pk)
    comments = Comment.objects.filter(post=blog)
    context = {
        'blog': blog,
        'comments': comments
    }
    # if request.POST:
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         form_data = form.save(commit=False)
    #         form_data.post = blog
    #         form_data.save()
    #         HttpResponseRedirect('')
    #     else:
    #         context['form'] = form
    # else:
    #     form = CommentForm()
    #     context['form'] = form
    if request.POST:
        author = request.POST.get("txtname")
        email = request.POST.get("txtemail")
        body = request.POST.get("txtmessage")
        comment = Comment.objects.create(post=blog, email=email, author=author, body=body)
        comment.save()
        HttpResponseRedirect("")
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


def events(request):
    event_list = Event.objects.all()
    event_image = EventImage.objects.all()
    # for event in event_list:
    #     print(event.is_past)
    context = {
        'event_list': event_list,
        'event_images': event_image
    }
    return render(request, 'events.html', context=context)



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

def team(request):
    members = Member.objects.filter(active=True)
    year = datetime.datetime.now().year
    batches_to_display = [year-1, year-2, year-3, year-4]
    alumni = Member.objects.filter(batch__in=batches_to_display)
    context = {
        'members': members,
        'batches_to_display': batches_to_display,
        'alumni': alumni
    }
    return render(request, 'team.html', context=context)