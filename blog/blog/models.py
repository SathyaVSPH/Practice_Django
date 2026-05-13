from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	#post_id = models.AutoField()
	title = models.CharField(max_length=60)
	#author = models.CharField(max_length=40)
	author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
	body = models.TextField()
	
	def __str__(self):
		return self.title[:50]
	
	def get_absolute_url(self):
		return reverse("post", kwargs={"pk":self.pk})
