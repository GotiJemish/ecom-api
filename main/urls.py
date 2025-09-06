from django.urls import path
# import views from current directory
from . import views  
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf.urls import include

router = DefaultRouter()
router.register('address', views.CustomerAddressViewSet, basename='customer-address')
router.register('product-review', views.ProductReviewViewSet, basename='product-reviews')



urlpatterns = [
    # define your url patterns here
    # path('example/' , example_view, name='example_view'), # Example URL pattern
    
    # vendors
path('vendors/', views.VendorList.as_view(), name='vendor-list'), # vendor list view
path('vendor/<int:pk>/', views.VendorDetail.as_view(), name='vendor-detail'), # vendor details view
# products
path('products/', views.ProductList.as_view(), name='product-list'), # vendor list view
path('product/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'), # vendor details view
# categories
path('categories/', views.CategoryList.as_view(), name='category-list'), # category list view
path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'), # category details view
# customers
path('customers/', views.CustomerList.as_view(), name='customer-list'), # customer list view
path('customer/<int:pk>/', views.CustomerDetail.as_view(), name='customer-detail'), # customer details view
# orders
path('orders/', views.OrderList.as_view(), name='order-list'), # order list view
path('order/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'), # order details view

# customer address routes

]

urlpatterns += router.urls  # include the router urls for customer address viewset