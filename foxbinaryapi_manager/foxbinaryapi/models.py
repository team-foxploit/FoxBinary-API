from django.db import models

# Create your models here.
class TickHistory(models.Model):
    prices = models.IntegerField()
    times = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
