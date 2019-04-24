from django.contrib import admin
from .models import TickHistory, BlogPost

# Register your models here.
admin.site.register(TickHistory)
admin.site.register(BlogPost)