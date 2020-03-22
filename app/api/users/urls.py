from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.urls import path, include

from .views import ProfileViewSet

router = DefaultRouter()
router.register(r'users', ProfileViewSet)

urlpatterns = [
    path('auth/', obtain_jwt_token),
    path('refresh/', refresh_jwt_token),
    path('verify/', verify_jwt_token),
    path('', include(router.urls)),
]
