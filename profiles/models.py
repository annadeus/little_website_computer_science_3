from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Information about the Profile of a User
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures')

    def __str__(self):
        return f"{self.user.username}'s Profile"
