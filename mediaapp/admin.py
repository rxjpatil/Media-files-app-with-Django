from django.contrib import admin
from mediaapp.models import Media

class MediaAdmin(admin.ModelAdmin):
    list_display=['name','type','format','size','duration_secs']

admin.site.register(Media,MediaAdmin)