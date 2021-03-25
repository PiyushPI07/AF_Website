from django.contrib import admin
from django.http import HttpResponse
from .models import *
# Register your models here.

class MemberDetails(admin.ModelAdmin):
    list_display = ('roll_number', 'member_name', 'batch', 'post')
    list_filter = ('batch', 'team', 'active')
    filter_horizontal = ()
    search_fields = ('member_name', 'roll_number')

# admin.site.register(ArtImage)
admin.site.register(EventImage)
admin.site.register(Member, MemberDetails)
admin.site.register(Event)
admin.site.register(Blog)
admin.site.register(Art)
admin.site.register(StaticContent)
admin.site.register(Udaan_image)
admin.site.register(Udaan_event)
admin.site.register(Comment)
