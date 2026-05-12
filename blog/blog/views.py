from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.
# ~ def all_posts(request):
	# ~ posts = models.Post.objects.all()
	# ~ return render(request, "all_posts.html", {"post_list":posts})

class AllPosts(ListView):
	model = models.Post
	template_name = "all_posts.html"	 
