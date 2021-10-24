from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title= models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    project_img=models.ImageField(upload_to='images/')
    project_url=models.URLField(max_length=200)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_photo=models.ImageField(upload_to='images/')

