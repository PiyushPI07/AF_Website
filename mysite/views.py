from django.shortcuts import render
from .models import *

def about(request):

    image_gallery_full = Image.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    context = {
               'image_gallery_full': image_gallery_full,
               'image_gallery_short': image_gallery_short,
               }
    return render(request, 'about.html', context=context)



# Create your views here.
