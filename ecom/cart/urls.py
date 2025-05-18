from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cart'  # Add this line

urlpatterns = [
  path('', views.cart_summary, name='cart_summary'),
  path('add/', views.cart_add, name='cart_add'),
  path('delete/', views.cart_delete, name='cart_delete'),
  path('update/', views.cart_update, name='cart_update'),
]
