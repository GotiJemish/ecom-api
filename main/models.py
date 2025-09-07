from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from versatileimagefield.fields import VersatileImageField


# vendor models
class Vendor(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) # it create forign key relationship with user model and if we delete user it will delete vendor also
    address=models.TextField(null=True, blank=True) # null and blank are used to make field optional

    def __str__(self):
        return self.user.username # __str__ method is used to return the username of the user from vendors when we print the object or in the admin panel


# products category models
class Category(models.Model):
    title=models.CharField(max_length=100) # max_length is required for CharField
    slug=models.CharField(max_length=100, unique=True) # slug is used to create url for the category
    description=models.TextField(null=True, blank=True) # description is optional

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title # __str__ method is used to return the title of the category when we print the object or in the admin panel


# product models
class Product(models.Model):
    title=models.CharField(max_length=100) # max_length is required for CharField
    slug=models.CharField(max_length=100, unique=True) # slug is used to create url for the product
    description=models.TextField(null=True, blank=True) # description is optional
    price=models.DecimalField(max_digits=10, decimal_places=2) # price is a decimal field with 10 digits and 2 decimal places
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category_products') # if we delete category it will make category null in all products in that category
    vendor=models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True) 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title # __str__ method is used to return the title of the product when we print the object or in the admin panel

# customer models

class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.username

# order models
class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_time=models.DateTimeField(auto_now_add=True)
    
# order items models
class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.title

# customer address models

class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_addresses")
    address_line1 = models.CharField(max_length=255, blank=False, null=False)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    default_address = models.BooleanField(default=False) # to mark default address
    # city = models.CharField(max_length=100, blank=False, null=False)
    # state = models.CharField(max_length=100, blank=False, null=False)
    # zip_code = models.CharField(max_length=20, blank=False, null=False)
    # country = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return f"{self.address_line1}"
    # {self.city}, {self.state}, {self.country}


# product review and rating model

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_reviews')
    customer =models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_reviews')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) # rating out of 5
    comment = models.TextField()
    current_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.rating} - {self.comment[:50]}" # return first 50 characters of comment
    
# Product Images models
class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products_images")
    image = VersatileImageField(upload_to='products_imgs/',null=True)

    def __str__(self):
        return f"{self.product}"
    # {self.city}, {self.state}, {self.country}