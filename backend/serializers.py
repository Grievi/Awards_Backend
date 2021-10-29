from typing_extensions import Required
from rest_framework import serializers
from backend.models import Profile, Project, Review
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


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

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username','password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
        'first_name': {'required': True},
        'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match!"})

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user