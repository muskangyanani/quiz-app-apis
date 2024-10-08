from rest_framework_simplejwt.views import TokenRefreshView 
from django.urls import path
from .views import MyTokenObtainPairView, RegisterView, userDetail, updateProfile

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('user/', userDetail, name='user_detail'),
    path('update-profile/', updateProfile, name='update_profile'),
]