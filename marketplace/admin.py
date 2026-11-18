from django.contrib import admin
from .models import Product, Review, Profile

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Review)

# Register your models here.
