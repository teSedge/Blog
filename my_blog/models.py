from django.db import models
# Create your models here.

class post(models.Model):
	title = models.CharField(max_length = 20)
	text_massegge = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'blog_images')
	date_time = models.DateTimeField(editable = False)
pass
