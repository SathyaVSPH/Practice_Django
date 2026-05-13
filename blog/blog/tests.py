from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from . import models

# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test_user",
            email="test@mail.com",
            password="secret",
        )
        cls.post = models.Post.objects.create(
            title="Just a title",
            author=cls.user,
            body="Sample Content",
        )
    
    def test_post_model(self):
        self.assertEqual(self.post.title, "Just a title")
        self.assertEqual(self.post.author.username, "test_user")
        self.assertEqual(self.post.body, "Sample Content")
        self.assertEqual(str(self.post), "Just a title") #for __str__
        self.assertEqual(self.post.get_absolute_url(), "/post/1/") #for get_absolute_url
    
    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)
    
    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200) #homepage check
        self.assertTemplateUsed(response, "all_posts.html") #template file check
        self.assertContains(response, "Sample Content") #template content check
    
    def test_post_detailview(self):
        response = self.client.get(reverse("post", kwargs={"pk":self.post.pk}))
        no_response = self.client.get("/post/10000000/")
        self.assertEqual(response.status_code, 200) #Details page check
        self.assertEqual(no_response.status_code, 404) #404 check
        self.assertContains(response, "Just a title")# template content check
        self.assertTemplateUsed(response, "post_page.html")#template file check