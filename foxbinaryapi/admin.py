from django.contrib import admin
from .models import TickHistory, BlogPost, APIToken

# Register your models here.
admin.site.register(TickHistory)
admin.site.register(BlogPost)
admin.site.register(APIToken)