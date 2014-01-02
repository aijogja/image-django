from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

class Gallery(models.Model):		
	image = models.ImageField(upload_to='gallery', blank=True, null=True)		
	image_thumb = ImageSpecField(source='image', processors=[ResizeToFill(100, 50)], format='PNG', options={'quality': 60})
	user = models.ForeignKey(User)

class Comment(models.Model):
	user = models.ForeignKey(User)
	gallery = models.ForeignKey(Gallery)
	comment = models.TextField(blank=True, null=True)
	tanggal = models.DateField(auto_now_add=True)
