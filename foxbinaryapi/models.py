from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class TickHistory(models.Model):
    price = models.IntegerField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.price

class BlogPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(max_length=300, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

# API token model
class APIToken(models.Model):
    token = models.CharField(max_length=500)
    owner = models.ForeignKey(User,
                              default=1,
                              related_name="api_tokens",
                              on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    
