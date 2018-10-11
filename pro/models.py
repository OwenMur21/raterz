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

    def __str__(self):
                return self.bio

class Project(models.Model):
    """
    Class that contains Project details
    """
    title = models.TextField()
    landing_page = models.ImageField(upload_to = 'images/')
    description = models.TextField()
    link = models.CharField(max_length = 30)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
                return self.bio



