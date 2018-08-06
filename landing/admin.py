from django.contrib import admin
from .models import *

class GamerAdmin (admin.ModelAdmin):
    list_display = ['login', 'password']

    class Meta:
        model = Gamer

admin.site.register(Gamer, GamerAdmin)