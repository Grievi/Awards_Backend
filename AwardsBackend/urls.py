from django.urls import path,include
from django.contrib import admin
from backend import views
from rest_framework import routers
from rest_framework.authtoken import views as token_views

router=routers.DefaultRouter()
router.register(r'Profile', views.ProfileApi)
router.register(r'Project',views.ProjectApi)
router.register(r'reviews', views.ReviewApi)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-login/', token_views.obtain_auth_token)
]
