from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Information about the Profile of a User

    user = one-to-one relationship with user -> each user can have exactly one profile
    bio = short description provided by user
    profile_picture = picture uploaded by the user to serve as profile picture
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures')

    """
    returns string of the profile 
    """
    def __str__(self):
        return f"{self.user.username}'s Profile"
