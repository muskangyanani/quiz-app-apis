from django.shortcuts import render
from .models import User, Profile
from userAuth.serializer import  MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView # type: ignore
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = ([AllowAny])
    serializer_class = RegisterSerializer 

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# # def dashboard(request):
#     if request.method == 'GET':
#         response = f"Welcome {request.user.username}"
#         return Response({'response': response}, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         text = request.data['text']
#         response = f"Welcome {request.user.username}. You sent: {text}"
#         return Response({'response': response}, status=status.HTTP_200_OK)
#     return Response({'response': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


# get user detail view
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userDetail(request):
    if request.method == 'GET':
        user = request.user
        profile = Profile.objects.get(user=user)
        response = {
            'username': user.username,
            'email': user.email,
            'full_name': profile.full_name
        }
        return Response({'response': response}, status=status.HTTP_200_OK)