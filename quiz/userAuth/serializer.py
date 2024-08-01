from rest_framework import serializers
from .models import User, Profile
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['full_name'] = user.profile.full_name
        token['username'] = user.username
        token['email'] = user.email
        return token
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
    
    def create(self, validated_data):
        if validated_data.email in User.objects.values_list('email', flat=True):
            raise serializers.ValidationError({"email": "Email already exists."})
        if validated_data.username in User.objects.values_list('username', flat=True):
            raise serializers.ValidationError({"username": "Username already exists."})
        
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user