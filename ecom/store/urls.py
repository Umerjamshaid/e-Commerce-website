from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'store'  # Add this line

urlpatterns = [
    path('', views.home ,name='home',),
    path('about/', views.about ,name='about',),
    path('login/', views.login_user ,name='login',),
    path('logout/', views.logout_user ,name='logout',),
    path('register/', views.register_user ,name='register',),
    # path('product/<int:pk>', views.product ,name='product',),
    path('product/<int:pk>/', views.product_view, name='product'),
    path('Dashboard/', views.Dashboard, name='Dashboard'),
    path('category/<str:foo>', views.category, name='category'),
]
