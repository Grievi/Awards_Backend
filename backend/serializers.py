from rest_framework import serializers
from backend.models import Profile, Project, Review

class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'