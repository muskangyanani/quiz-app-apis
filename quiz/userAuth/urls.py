from rest_framework_simplejwt.views import TokenRefreshView 
from django.urls import path
from .views import MyTokenObtainPairView, RegisterView, userDetail

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('user/', userDetail, name='user_detail')
    # path('dashboard/', dashboard, name='dashboard'),
]