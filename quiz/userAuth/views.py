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
    try:
        profile = request.user.profile
        data = request.data
        
        # Update full_name and image if they are provided in the request
        if 'full_name' in data:
            profile.full_name = data['full_name']
        if 'image' in data:
            profile.image = data['image']

        profile.save()

        # Serialize the updated profile and return it in the response
        serializer = ProfileSerializer(profile)
        return Response({"response": serializer.data}, status=status.HTTP_200_OK)

    except Profile.DoesNotExist:
        return Response({"error": "Profile does not exist"}, status=status.HTTP_400_BAD_REQUEST)