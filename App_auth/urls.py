from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from App_auth.views import *

urlpatterns = [
    path('signup/', RegistrationAPIView.as_view(), name='register'),
    path('login/token/', TokenObtainPairView.as_view()),
    path('login/token/refresh/', TokenRefreshView.as_view()),
]
