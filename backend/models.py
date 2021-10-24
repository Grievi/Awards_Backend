from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_photo=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=155)
    bio=models.CharField(max_length=255)
    projects=models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username}Profile '

    def save_profile(self):
        self.save()

class Project(models.Model):
    title= models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    project_img=models.ImageField(upload_to='images/')
    project_url=models.URLField(max_length=200)
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

class Review(models.Model):
    Rating=[
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'),
    ]
    Design=models.CharField(max_length=100,choices=Rating, default='rate' ),
    Usability=models.CharField(max_length=100,choices=Rating, default='rate' )
    Content=models.CharField(max_length=100,choices=Rating, default='rate' )
    average=models.FloatField(default=0, blank=True)

    def __str__(self):
        return self.average

    


