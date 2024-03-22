from django.db import models
from web_user.models import CustomUser

class Post(models.Model):
    post_id = models.AutoField(primary_key=True, editable=False)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

class Media(models.Model):
    media_id = models.AutoField(primary_key=True, editable=False)
    media_file = models.ImageField(upload_to='media/', null=True)
    posts = models.ManyToManyField(Post, related_name='media_files')

    def __str__(self):
        return f"Media ID: {self.media_id}"
