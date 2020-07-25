from django.db import models

# Create your models here.
class Sound(models.Model):
    on = models.BooleanField(default=True)