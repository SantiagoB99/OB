from django.contrib import admin

from .models import *


admin.site.register(Movie)
admin.site.register(MovieInstance)
admin.site.register(Director)
admin.site.register(Genre)