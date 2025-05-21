from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('vendor/', views.VendorListCreate.as_view(), name='vendor-list-create'),
    path('vendor/<int:pk>/', views.VendorDetail.as_view(), name='vendor-detail'),
    path('products/', views.ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),



    # Registration
    path('user/register/', views.UserRegisterView.as_view(), name='register-user'),
    path('vendor/register/', views.VendorRegisterView.as_view(), name='register-vendor'),
    path('admin/register/', views.AdminRegisterView.as_view(), name='register-admin'),

    # Login by role
    path('user/login/', views.UserLoginView.as_view(), name='user-login'),
    path('vendor/login/', views.VendorLoginView.as_view(), name='vendor-login'),
    path('admin/login/', views.AdminLoginView.as_view(), name='admin-login'),

   ]
