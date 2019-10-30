from django.db import models
import datetime

# Create your models here.
class Blog(models.Model):
	title=models.CharField(max_length=250)
	pub_date=models.DateTimeField()
	text=models.TextField()
	image=models.ImageField(upload_to='MEDIA_ROOT')

