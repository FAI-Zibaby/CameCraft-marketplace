from django.shortcuts import render
from .models import Product

def home(request):
    # Fetch all products from the database
    products = Product.objects.all().order_by('-created_at')
    
    # Pass them to the template
    context = {
        'products': products
    }
    return render(request, 'marketplace/home.html', context)