from django.contrib import admin
from . import models

admin.site.register(models.Vendor) # registering the vendor model with the admin site 
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.CustomerAddress)
admin.site.register(models.ProductReview)

