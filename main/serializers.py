from rest_framework import serializers
# importing models from same directory
from . import models 


# vendor serializers
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor # specify the model to be serialized
        # fields = '__all__'
        fields = ['id','user', 'address']
        # depth = 1 
    def __init__(self, *args, **kwargs):
        super(VendorSerializer, self).__init__(*args, **kwargs)
        # request = self.context.get('request', None)
        # self.Meta.depth = 1 

class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor # specify the model to be serialized
        fields = ['id', 'user', 'address']
        # depth = 1
         
    def __init__(self, *args, **kwargs):
        super(VendorDetailSerializer, self).__init__(*args, **kwargs)
        # request = self.context.get('request', None)
        # self.Meta.depth = 1 
   
# category serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category # specify the model to be serialized
        # fields = '__all__'
        fields = ['id','title','description']
        # depth = 1 
    def __init__(self, *args, **kwargs):
        super(CategorySerializer, self).__init__(*args, **kwargs)
        # request = self.context.get('request', None)
        # self.Meta.depth = 1 
        
class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category # specify the model to be serialized
        fields = ['id','title','description']
        # depth = 1
         
    def __init__(self, *args, **kwargs):
        super(CategoryDetailSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request', None)
        self.Meta.depth = 1 
   
        
# product serializers
class ProductListSerializer(serializers.ModelSerializer):
    product_reviews = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Product # specify the model to be serialized
        # fields = '__all__'
        fields = ['id','title','price','category','vendor','product_reviews','tag_list']
        # depth = 1 
    def __init__(self, *args, **kwargs):
        super(ProductListSerializer, self).__init__(*args, **kwargs)
        # request = self.context.get('request', None)
        # self.Meta.depth = 1 

#  product image serializers
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImages
        fields =["id", "product", "image" ]
        # depth = 1


class ProductDetailSerializer(serializers.ModelSerializer):
    product_reviews = serializers.StringRelatedField(many=True, read_only=True)   # to get the product reviews in the product details
    category=CategorySerializer(read_only=True) # to get the cateory details in the product details
    vendor=VendorSerializer(read_only=True)
    products_images=ProductImageSerializer(many=True, read_only=True)
    # customer_reviews = ProductReviewSerializer(many=True, read_only=True)

    class Meta:
        model = models.Product # specify the model to be serialized
        fields = [ 'id', 'title', 'description','price','category','vendor','product_reviews','products_images','tag_list' ]
        depth = 1
         
    def __init__(self, *args, **kwargs):
        super(ProductDetailSerializer, self).__init__(*args, **kwargs)
        # request = self.context.get('request', None)
        # self.Meta.depth = 1 
      
# vendor serializers
class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer # specify the model to be serialized
        # fields = '__all__'
        fields = ['id','user', 'mobile']
        # depth = 1 
    def __init__(self, *args, **kwargs):
        super(CustomerListSerializer, self).__init__(*args, **kwargs)
        # request = self.context.get('request', None)
        # self.Meta.depth = 1 

class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer # specify the model to be serialized
        fields = ['id', 'user', 'mobile']
        depth = 1
         
    def __init__(self, *args, **kwargs):
        super(CustomerDetailSerializer, self).__init__(*args, **kwargs)
        # request = self.context.get('request', None)
        # self.Meta.depth = 1 
   
# order serializers
class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ["id", "customer", "order_time"]
        depth = 1
        
    def __init__(self, *args, **kwargs):
        super(OrderListSerializer, self).__init__(*args, **kwargs)


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = ["id", "order", "product"]
        depth = 1
        
    def __init__(self, *args, **kwargs):
        super(OrderDetailSerializer, self).__init__(*args, **kwargs)
        
        
        
# customer address serialiers
class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerAddress
        fields =["id", "customer", "address_line1", "address_line2",
                #  "city", "state", "zip_code", "country"
                 ]
        depth = 1
    
    def __init__(self, *args, **kwargs):
        super(CustomerAddressSerializer, self).__init__(*args, **kwargs)
        
#  product review serializers
class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductReview
        fields =["id", "product", "customer", "rating", "comment", "current_time", ]
        depth = 1
    
    def __init__(self, *args, **kwargs):
        super(ProductReviewSerializer, self).__init__(*args, **kwargs)

