from django.shortcuts import render
from .models import User, Profile
from userAuth.serializer import  MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView # type: ignore
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from userAuth.serializer import ProfileSerializer
from userAuth.models import Profile
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = ([AllowAny])
    serializer_class = RegisterSerializer 

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
    

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == 'PATCH':
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            user.username = request.data.get('username', user.username)
            user.save()
            response = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'full_name': profile.full_name,
                'image': str(profile.image.url) if profile.image else None
            }
            return Response({'response': response}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)