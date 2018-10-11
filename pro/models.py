from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    """
    Class that contains Profile details
    """
    profile_pic = models.ImageField(upload_to = 'images/', blank=True)
    bio = models.TextField()
    contact = models.CharField(max_length = 30, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


