from django.db import models

# Create your models here.
class TickHistory(models.Model):
    price = models.IntegerField()
    time = models.DateTimeField(unique=True)
    accessed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.price
