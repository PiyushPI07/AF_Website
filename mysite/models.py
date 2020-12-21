from django.db import models
from django.urls import reverse


class Member(models.Model):
    roll_number = models.CharField(max_length=8, primary_key=True)
    member_name = models.CharField(max_length=25)
    post = models.CharField(max_length=300)
    insta = models.URLField(default=" ")
    email = models.EmailField(max_length = 50,default=" ")
    linkedin = models.URLField(default=" ")
    head = models.BooleanField(default=False)
    testimonial = models.TextField(default=" ")
    member_img = models.ImageField(upload_to='images/members')

    def __str__(self):
        return self.member_name


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default=" ")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Art(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='art_posts')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=30)
    blog_filter = models.IntegerField(default=0)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    blog_img = models.ImageField(upload_to='images/blog')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class EventImage(models.Model):
    img = models.ImageField(upload_to='images/event')
    title = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_posts')

    def __str__(self):
        return self.title


class ArtImage(models.Model):
    art_image = models.ImageField(upload_to='images/art')
    title = models.ForeignKey(Art, on_delete=models.CASCADE, related_name='art_posts')

    def __str__(self):
        return self.title

# Create your models here.
#Udaan model
class Udaan_static(models.Model):
    main_description= models.TextField()
    date= models.DateTimeField( auto_now=False, auto_now_add=False, null = True)
    def __str__(self):
        return self.main_description


class Udaan_image(models.Model):
    img_name = models.CharField( max_length=50)
    img = models.ImageField( upload_to='images/udaan/carousel', height_field=None, width_field=None, max_length=None)
    alt_text = models.CharField( max_length=50)
    display_on_caurosel = models.BooleanField(default = False)

    def __str__(self):
        return self.alt_text

class Udaan_event(models.Model):
    event_name= models.CharField( max_length=50)
    event_description= models.TextField()
    event_img= models.ImageField( upload_to='images/udaan/events', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.event_name   

class Gallery(models.Model):
    description = models.TextField(default=" ")
    image = models.ImageField(upload_to='images/gallery')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
