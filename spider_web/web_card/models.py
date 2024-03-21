from django.db import models
from web_user.models import CustomUser

class Post(models.Model):
    post_id = models.AutoField(primary_key=True, editable=False)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

class Media(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    media_file = models.ImageField(upload_to='media/', null=True)
    # Add any other fields related to media here

# class Ranker(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     ranker_name = models.CharField(max_length=100)

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     comment_text = models.TextField()
#     time = models.DateTimeField(auto_now_add=True)
#     is_local = models.BooleanField(default=False)  


    def __str__(self):
        return str(self.id)
