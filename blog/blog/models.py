from django.db import models

# Create your models here.
class Post(models.Model):
	#post_id = models.AutoField()
	title = models.CharField(max_length=60)
	author = models.CharField(max_length=40)
	body = models.TextField()
	
	def __str__(self):
		return f"Title: {self.title[:50]}"
