from django.db import models


class Image(models.Model):
    img = models.ImageField(upload_to='images/gallery')
    alt_text = models.CharField(max_length=50)
    display_on_index = models.BooleanField()

    def __str__(self):
        return self.alt_text


class Event(models.Model):
    page_to_display = models.IntegerField(default=0)
    bg_img = models.ImageField(upload_to='images/event')
    small_text = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.small_text


class Member(models.Model):
    roll_number = models.CharField(max_length=8, primary_key=True)
    member_name = models.CharField(max_length=50)
    post = models.CharField(max_length=300)
    insta = models.URLField(default=" ")
    linkdin = models.URLField(default=" ")
    head = models.BooleanField(default=False)
    testimonial = models.TextField(default=" ")
    member_img = models.ImageField(upload_to='images/members')

    def __str__(self):
        return self.member_name


class Blog(models.Model):
    title = models.CharField(max_length=50, unique=True)
    blog_filter = models.IntegerField(default=0)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    blog_img = models.ImageField(upload_to='images/blogs', null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Art(models.Model):
    title = models.CharField(max_length=50, unique=True)
    art_filter = models.IntegerField(default=0)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='art_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    art_img = models.ImageField(upload_to='images/art')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

# Create your models here.
