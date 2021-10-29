from django.contrib.auth.models import User
from backend.models import Profile, Project,Review
from backend.serializers import ProfileSerializer, ProjectSerializer, ReviewSerializer,RegisterSerializer
from rest_framework import viewsets,permissions

class ProfileApi(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[permissions.AllowAny]

class ProjectApi(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    permission_classes=[permissions.AllowAny]

    
class ReviewApi(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[permissions.AllowAny]

class RegisterView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=[permissions.AllowAny]

