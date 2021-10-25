from django.shortcuts import render
from backend.models import Profile, Project,Review
from backend.serializers import ProfileSerializer, ProjectSerializer, ReviewSerializer
from rest_framework import viewsets,permissions

class ProfileApi(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    

class ProjectApi(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    

class ReviewApi(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

