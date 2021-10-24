from django.contrib import admin
from backend.models import Profile, Project,Review

admin.site.regiter(Profile)
admin.site.regiter(Project)
admin.site.regiter(Review)

