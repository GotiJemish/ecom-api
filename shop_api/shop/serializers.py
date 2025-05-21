from rest_framework import serializers
from .models import Vendor, Product, UserProfile
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'vendor', 'name', 'description', 'price']




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'vendor', 'name', 'description', 'price']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class VendorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Vendor
        fields = ['id', 'user', 'company_name']


# General user registration
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        UserProfile.objects.create(user=user, role='user')
        return user


# Vendor registration
class VendorRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    company_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'company_name']

    def create(self, validated_data):
        company_name = validated_data.pop('company_name')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, role='vendor')
        Vendor.objects.create(user=user, company_name=company_name)
        return user


# Admin registration
class AdminRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_superuser(**validated_data)
        UserProfile.objects.create(user=user, role='admin')
        return user







class RoleBasedTokenSerializer(TokenObtainPairSerializer):
    expected_role = None  # to be set dynamically by each login view

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        try:
            profile = user.userprofile
        except UserProfile.DoesNotExist:
            raise AuthenticationFailed("User profile not found.")

        if self.expected_role and profile.role != self.expected_role:
            raise AuthenticationFailed(f"This login is only for '{self.expected_role}' users.")

        data['role'] = profile.role
        return data
