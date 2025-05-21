from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Vendor, Product
from .serializers import (
    VendorSerializer,
    ProductSerializer,
    UserSerializer,
    UserRegisterSerializer,
    VendorRegisterSerializer,
    AdminRegisterSerializer
)
from rest_framework_simplejwt.views import TokenObtainPairView

# Custom Token Serializer with Role Validation
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from .models import UserProfile



# Vendor Views
class VendorListCreate(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


# Product Views
class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Register Views
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


class VendorRegisterView(generics.CreateAPIView):
    serializer_class = VendorRegisterSerializer
    permission_classes = [AllowAny]


class AdminRegisterView(generics.CreateAPIView):
    serializer_class = AdminRegisterSerializer
    permission_classes = [AllowAny]




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



# Login Views by Role
class UserLoginView(TokenObtainPairView):
    serializer_class = type('UserTokenSerializer', (RoleBasedTokenSerializer,), {
        'expected_role': 'user'
    })

class VendorLoginView(TokenObtainPairView):
    serializer_class = type('VendorTokenSerializer', (RoleBasedTokenSerializer,), {
        'expected_role': 'vendor'
    })

class AdminLoginView(TokenObtainPairView):
    serializer_class = type('AdminTokenSerializer', (RoleBasedTokenSerializer,), {
        'expected_role': 'admin'
    })
