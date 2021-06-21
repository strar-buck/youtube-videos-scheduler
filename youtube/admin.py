from django.contrib import admin

from .models import YoutubeVideoCredential, YoutubeVideo

admin.site.register(YoutubeVideoCredential)
admin.site.register(YoutubeVideo)
