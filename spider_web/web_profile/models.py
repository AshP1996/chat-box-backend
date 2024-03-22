from django.db import models
from django.utils import timezone
from web_user.models import CustomUser

class Profile(models.Model):
    id_profile = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='profiles')
    user_name = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    links = models.URLField(max_length=200, blank=True)
   

    def __str__(self):
        return self.user_name
