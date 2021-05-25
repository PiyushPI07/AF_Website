from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from account.forms import VolunteerForm, SandArtRegistrationForm
from django.views.decorators.cache import cache_control
from django.shortcuts import get_object_or_404, render
from .forms import CommentForm
from .models import *


def index(request):
    full_member_list = Member.objects.all()
    art_list = Art.objects.all()
    recruitments = True
    # art_image = ArtImage.objects.all()
    image_gallery_short = ''
    event_list = []
    context = {
        'full_member_list': full_member_list,
        'art_list': art_list,
        'event_list': event_list,
        'image_gallery_short': image_gallery_short,
        'render_recruitment_form': True,
        'recruitments': recruitments
        # 'art_image': art_image,
    }
    return render(request, 'index.html', context=context)


def about(request):
    year = datetime.datetime.now().year
    batches_to_display = [year-1, year-2, year-3, year-4]
    testimonials = Member.objects.filter(batch__in=batches_to_display).exclude(testimonial='')
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
    if request.POST:
        author = request.POST.get("txtname")
        email = request.POST.get("txtemail")
        body = request.POST.get("txtmessage")
        comment = Comment.objects.create(post=blog, email=email, author=author, body=body)
        comment.save()
        HttpResponseRedirect("")
    return render(request, 'blog_post.html', context=context)


def udaan_view(request, *args, **kwargs):
    if StaticContent.objects.count() == 0:
        return HttpResponseNotFound("<h1>Page not found</h1>")
    static_data= StaticContent.objects.first()
    carousel_imgs = Udaan_image.objects.filter(display_on_caurosel = True)
    events = Udaan_event.objects.all()
    context = {
        'desc': static_data.udaan_description,
        'date': static_data.udaan_date.month,
        'form_open': static_data.sand_art_form,
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

def check_back_later(request, t):
    if StaticContent.objects.count():
        dates = StaticContent.objects.first()
        if t == 's_art404':
            disp_text = 'Sand Art Competition Registrations'
            date = dates.udaan_date.strftime('%B')
        if t == 'recs404':
            disp_text = 'Recruitments'
            date = dates.recs_date.strftime('%B')
    else:
        if t == 's_art404':
            disp_text = 'Sand Art Competition Registrations'
            date = "January"
        if t == 'recs404':
            disp_text = 'Recruitments'
            date = "August"
        
    context = {
        'disp_text': disp_text,
        'date': date
    }
    return render(request, 'check_back_later.html', context=context)

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
    members = Member.objects.filter(active=True).order_by('post', 'batch', 'member_name')
    year = datetime.datetime.now().year
    batches_to_display = [year-1, year-2, year-3]
    exc_members = members.filter(team="")
    core_members = members.filter(team="Core")
    mnc_members = members.filter(team__in=["Media and Content Team", "Both Media and Website Team"])
    web_members = members.filter(team__in=["Website Team", "Both Media and Website Team"])
    alumni = Member.objects.filter(batch__in=batches_to_display).order_by('post', 'member_name')
    context = {
        'members': members,
        'batches_to_display': batches_to_display,
        'alumni': alumni,
        'executive_members': exc_members,
        'core_members' : core_members,
        'med_and_content_members': mnc_members,
        'web_members' : web_members
    }
    return render(request, 'team.html', context=context)