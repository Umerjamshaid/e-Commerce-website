from django.shortcuts import render, redirect
from .models import Category, Customer, Product, Order
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
from django.shortcuts import render, get_object_or_404
from django.conf.urls.static import static



def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {'product': product})


def home(request):
    products = Product.objects.all()  
    return render(request, 'home.html', {'products': products})


def about(request):
     return render(request, 'about.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully.')
            return redirect('store:home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('store:login')


    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('store:home')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been registered successfully.')
            return redirect('store:home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
            return redirect('store:register')
    else:
       return render(request, 'register.html', {'form': form})



def Dashboard(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'Dashboard.html', {})  #



def category(request, foo):
    # Replace hyphens with spaces
    foo = foo.replace('-', ' ')
    
    try:
        # Get category and products (correct filter field name)
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)  # Lowercase 'category' (match your model field name)
        return render(request, 'Category.html', {'products': products, 'category': category})  # Fix context dictionary
    except Category.DoesNotExist:
        messages.error(request, 'Category not found.')  # Fix messages call
        return redirect('store:home')