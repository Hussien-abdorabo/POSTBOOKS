from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    # ------------- method to get the count of comments ---------
    def comment_count(self):
        return self.comment_set.all().count()
    
    # --------------method to get all comment -------------------
    def comments(self):
        return self.comment_set.all()
    

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        ordering = ("-date",)
        verbose_name_plural = "Posts"



class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=100)