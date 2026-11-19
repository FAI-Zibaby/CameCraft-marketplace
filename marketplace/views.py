from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages
from .forms import UserRegisterForm # <--- Import the new form


def home(request):
    # Fetch all products from the database
    products = Product.objects.all().order_by('-created_at')
    
    # Pass them to the template
    context = {
        'products': products
    }
    return render(request, 'marketplace/home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created for {user.username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def artisan_dashboard(request):
    # Security check: Only artisans can see this page
    if request.user.profile.role != 'artisan':
        messages.error(request, "You do not have permission to view this page.")
        return redirect('home')
    
    # You will add product upload logic here later
    return render(request, 'marketplace/artisan_dashboard.html')

@login_required
def buyer_dashboard(request):
    # Buyers just see their orders (which we will build later)
    return render(request, 'marketplace/buyer_dashboard.html')