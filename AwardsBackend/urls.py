from django.urls import path,include
from django.contrib import admin
from backend import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'Profile', views.ProfileApi)
router.register(r'Project',views.ProjectApi)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework'))
]
