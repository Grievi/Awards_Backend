from rest_framework import serializers
from backend.models import Profile, Project, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model =Review
        fields='__all__'

class ProjectSerializer(serializers.ModelSerializer):
    proj_performance=ReviewSerializer(read_only=True, many=True)
    class Meta:
        model=Project
        fields='__all__'


class ProfileSerializer(serializers.ModelSerializer):
    projects=ProjectSerializer(read_only=True, many=True)
    class Meta:
        model=Profile
        fields='__all__'