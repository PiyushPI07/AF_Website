import sys
from django.db import models
from django.urls import reverse
import datetime
from django.utils import timezone
import pytz
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import MaxValueValidator, MinValueValidator

utc=pytz.UTC

class Member(models.Model):
    CON = 0
    JCON = 1
    PRESI = 2
    VPRESI = 3
    SECR = 4
    CHAIR = 5
    WEBH = 6
    CCO = 7
    CRCO = 8
    PR = 9
    ECO = 10
    PMC = 11
    WC = 12
    EXM = 13

    POST_CHOICES = [
        (CON, "Convener"),
        (JCON, "Joint Convener"),
        (PRESI, "President"),
        (VPRESI, "Vice President"),
        (SECR, "Secretary"),
        (CHAIR, "Chair"),
        (WEBH, "Website Head"),
        (CCO, "Chief Co-ordinator"),
        (CRCO, "Creative Co-ordinator"),
        (PR, "Public Relations Head"),
        (ECO, "Events Co-ordinator"),
        (PMC, "Publicity and Media Co-ordinator"),
        (WC, "Workshops Co-ordinator"),
        (EXM, "Executive Member")
    ]

    CORE = "Core"
    MCT = "Media and Content Team"
    WEB = "Website Team"
    BTH = "Both Media and Website Team"

    TEAM_CHOICES = [
        (CORE, "Core"),
        (MCT, "Media and Content Team"),
        (WEB, "Website Team"),
        (BTH, "Both Media and Website Team")
    ]
    roll_number = models.CharField(max_length=8, primary_key=True)
    member_name = models.CharField(max_length=25)
    post = models.IntegerField(choices=POST_CHOICES, default=13)
    insta = models.URLField(verbose_name="Instagram profile URL", blank=True)
    email = models.EmailField(max_length = 50,default=" ")
    batch = models.CharField(verbose_name='Batch', max_length=4, help_text="passing year")
    # curr_core = models.BooleanField(default=False, help_text="Is this member current core member?")
    team = models.CharField(verbose_name="Executive Team", max_length=50, choices=TEAM_CHOICES, blank=True)
    testimonial = models.TextField(default=" ", blank=True)
    member_img = models.ImageField(upload_to='images/members')
    def save(self, *args, **kwargs):
        if self.roll_number:
            self.member_img = self.compress_image(self.member_img)
        super(Member, self).save(*args, **kwargs)
    
    def compress_image(self, member_img):
        image_temporary = Image.open(member_img)
        output_io_stream = BytesIO()
        # image_temp_resized = image_temporary.resize((440, 650))                        #Resize to keep a consistent image size
        image_temporary.save(output_io_stream, format = 'JPEG', quality=30)         #lossless compression
        output_io_stream.seek(0)
        member_img = InMemoryUploadedFile(output_io_stream,'ImageField', "%s.jpg" % member_img.name.split('.')[0], 'image/jpeg', sys.getsizeof(output_io_stream), None)
        return member_img
    active = models.BooleanField(verbose_name="member status", default=True)
    class Meta:
        ordering = ['batch', 'member_name', 'post']
    def __str__(self):
        return self.member_name
    @property
    def alumni_filter(self):
        curr_year = datetime.datetime.now().year
        return self.batch + 4 < curr_year and self.batch < curr_year
    @property
    def core_filter(self):
        return self.curr_core and self.active

class Event(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(default=" ")
    date = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    @property
    def is_past(self):
        if self.date:
            utc_date = utc.localize(datetime.datetime.now())
            return utc_date > self.date
        else:
            return False

    def __str__(self):
        return self.title


class Art(models.Model):
    SKT = 'Sketches'
    DDL = 'Doodles'
    ABS = 'Abstract'
    ANIM = 'Anime'
    PRT = 'Portrait'
    NTR = 'Nature'
    DGT = 'Digital'
    OTR = 'Other'
    art_choices = [
        (SKT, 'Sketches'),
        (DDL, 'Doodles'),
        (ANIM, 'Anime'),
        (ABS, 'Abstract'),
        (PRT, 'Portrait'),
        (NTR, 'Nature'),
        (DGT, 'Digital'),
        (OTR, 'Other')
    ]
    art_image = models.ImageField(upload_to='images/art')

    def save(self, *args, **kwargs):
        if not self.id:
            self.art_image = self.compress_image(self.art_image)
        super(Art, self).save(*args, **kwargs)
    
    def compress_image(self, art_image):
        image_temporary = Image.open(art_image)
        output_io_stream = BytesIO()
        image_temporary.save(output_io_stream, format = 'JPEG', quality=30)         #lossless compression
        output_io_stream.seek(0)
        art_image = InMemoryUploadedFile(output_io_stream,'ImageField', "%s.jpg" % art_image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output_io_stream), None)
        return art_image


    title = models.CharField(max_length=20)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='art_posts')
    score = models.IntegerField(
        verbose_name="Score",
        default= 1,
        validators=[MaxValueValidator(10), MinValueValidator(0)] 
        )
    created_on = models.DateTimeField(auto_now_add=True)
    art_type = models.CharField(verbose_name='Type', max_length=20, choices=art_choices)
    class Meta:
        ordering = ['-score', '-created_on']

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
    def save(self, *args, **kwargs):
        if not self.id:
            self.blog_img = self.compress_image(self.blog_img)
        super(Blog, self).save(*args, **kwargs)
    
    def compress_image(self, blog_img):
        image_temporary = Image.open(blog_img)
        output_io_stream = BytesIO()
        image_temporary.save(output_io_stream, format = 'JPEG', quality=40)         #lossless compression
        output_io_stream.seek(0)
        blog_img = InMemoryUploadedFile(output_io_stream,'ImageField', "%s.jpg" % blog_img.name.split('.')[0], 'image/jpeg', sys.getsizeof(output_io_stream), None)
        return blog_img
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class EventImage(models.Model):
    img = models.ImageField(upload_to='images/event')
    title = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_posts')

    def __str__(self):
        return self.title.title


#Udaan model
class StaticContent(models.Model):
    udaan_description= models.TextField()
    udaan_date= models.DateTimeField( auto_now=False, auto_now_add=False, null = True)
    sand_art_form = models.BooleanField(verbose_name="Sand Art Competion form open", default=False, help_text="Check if Sand Art Competition form is to be displayed.")
    recs_date= models.DateField( auto_now=False, auto_now_add=False, null = True)
    recs_form = models.BooleanField(verbose_name="Recruitment form open", default=False, help_text="Check if we recruitments form is to be displayed")



class Udaan_image(models.Model):
    img_name = models.CharField( max_length=50)
    img = models.ImageField( upload_to='images/udaan/carousel', height_field=None, width_field=None, max_length=None)
    alt_text = models.CharField( max_length=50)
    display_on_caurosel = models.BooleanField(default = False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.img = self.compress_image(self.img)
        super(Udaan_image, self).save(*args, **kwargs)
    
    def compress_image(self, img):
        image_temporary = Image.open(img)
        output_io_stream = BytesIO()
        image_temporary.save(output_io_stream, format = 'JPEG', quality=30)         #lossless compression
        output_io_stream.seek(0)
        img = InMemoryUploadedFile(output_io_stream,'ImageField', "%s.jpg" % img.name.split('.')[0], 'image/jpeg', sys.getsizeof(output_io_stream), None)
        return img
    def __str__(self):
        return self.alt_text

class Udaan_event(models.Model):
    event_name= models.CharField( max_length=50)
    event_description= models.TextField()
    event_img= models.ImageField( upload_to='images/udaan/events', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.event_name   


class Comment(models.Model):
    post = models.ForeignKey(to=Blog, on_delete=models.CASCADE, related_name='post_comment')
    author = models.CharField(verbose_name='author', max_length=30, blank=False)
    body = models.TextField(verbose_name='Post Comment')
    email = models.EmailField(verbose_name='email')
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_on']

    def __str__(self):
        return self.body
