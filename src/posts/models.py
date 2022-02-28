from distutils.text_file import TextFile
from django.db import models
from django.shortcuts import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    
    
class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.post
    
    @property
    def get_comment_count(self):
        comment_count = self.comment_set.all().count()
        
    @property
    def get_like_count(self):
        like_count = self.like_set.all().count()
    
    @property
    def get_view_count (self):
        view_count = self.view_set.all().count()

class PostView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.post
    
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.post