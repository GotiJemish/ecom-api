from rest_framework import generics,permissions,pagination,viewsets
from . import serializers
from django.shortcuts import get_object_or_404
from . import models


# vendor list view
class  VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all() # get all vendors
    serializer_class = serializers.VendorSerializer   # specify the serializers class to be used for serialization
    # permission_classes=[permissions.IsAuthenticated]
    
# vendor detail view 
class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vendor.objects.all() # get all vendors
    serializer_class = serializers.VendorDetailSerializer   # specify the serializers class to be used for serialization
    # permission_classes=[permissions.IsAuthenticated]
    
#  product list view
class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all() # get all products
    serializer_class = serializers.ProductListSerializer   # specify the serializers class to be used for serialization
     # permission_classes=[permissions.IsAuthenticated]
    # pagination_class=pagination.LimitOffsetPagination  # using this we can apply different pagination then whole application default pagination
     

# product detail view
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all() # get all vendors
    serializer_class = serializers.ProductDetailSerializer   # specify the serializers class to be used for serialization
    # permission_classes=[permissions.IsAuthenticated]
    
    
    
 #  category list view
class CategoryList(generics.ListCreateAPIView):
    queryset = models.Category.objects.all() # get all categories
    serializer_class = serializers.CategorySerializer   # specify the serializers class to be used for serialization
     # permission_classes=[permissions.IsAuthenticated]
    # pagination_class=pagination.LimitOffsetPagination  # using this we can apply different pagination then whole application default pagination
     

# category detail view
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all() # get all vendors
    serializer_class = serializers.CategoryDetailSerializer   # specify the serializers class to be used for serialization
    # permission_classes=[permissions.IsAuthenticated]   
    
    
# customer list view
class CustomerList(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all() # get all vendors
    serializer_class = serializers.CustomerListSerializer   # specify the serializers class to be used for serialization
    # permission_classes=[permissions.IsAuthenticated]
    
# customer detail view 
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Customer.objects.all() # get all vendors
    serializer_class = serializers.CustomerDetailSerializer   # specify the serializers class to be used for serialization
    # permission_classes=[permissions.IsAuthenticated]
    
    
# order list view
class OrderList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all() # get all vendors
    serializer_class = serializers.OrderListSerializer   # specify the serializers class to be used for serialization
    # permission_classes=[permissions.IsAuthenticated]
    
    
# order detail view 
class OrderDetail(generics.ListAPIView):
    # queryset = models.OrderItem.objects.all() # get all orders
    serializer_class = serializers.OrderDetailSerializer   # specify the serializers class to be used for serialization
    # permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        order_id = self.kwargs.get('pk')   # get the order id from the url kwargs
        order = get_object_or_404(models.Order, id=order_id) # get the order object using the order id
        order_items=models.OrderItem.objects.filter(order=order)  # filter orders by order
        return order_items
    
# customer address view
class CustomerAddressViewSet(viewsets.ModelViewSet):
    queryset = models.CustomerAddress.objects.all() # get all customer adddresses
    serializer_class = serializers.CustomerAddressSerializer
    
    # def get_queryset(self):
    #     customer_id = self.kwargs.get('pk')   # get the customer id from the url kwargs
    #     order = get_object_or_404(models.Order, id=order_id) # get the order object using the order id
    #     order_items=models.OrderItem.objects.filter(order=order)  # filter orders by order
    #     return order_items
    
    
# prduct review view
class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = models.ProductReview.objects.all() # get all poduct reviews
    serializer_class = serializers.ProductReviewSerializer