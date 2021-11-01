from rest_framework import serializers
from backend.models import Profile, Project, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model =Review
        fields=[
            'project_perfomance',
            'Design',
            'Usability',
            'Content',
            'average',
        ]

class ProjectSerializer(serializers.ModelSerializer):
    proj_performance=ReviewSerializer(read_only=True, many=True)
    class Meta:
        model=Project
        fields=[
            'user',
            'project_name',
            'description',
            'project_img',
            'project_url',
            'proj_performance'
        ]
        read_only_fields=['user']

class ProfileSerializer(serializers.ModelSerializer):
    projects=ProjectSerializer(read_only=True, many=True)
    class Meta:
        model=Profile
        fields=[
            'user',
            'username',
            'profile_photo',
            'bio',
            'projects',
        ]
        read_only_fields=['user']

