from django.db import models
from django.conf import settings

# Create your models here.
class Job(models.Model):
	image=models.ImageField(upload_to='MEDIA_ROOT')
	summary=models.CharField(max_length=200)

