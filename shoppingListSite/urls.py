"""
URL configuration for shoppingListSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shopping_list import views
from django.urls import path
from shopping_list.views import login_view ,logout_view,signup_view
from django.urls import path





urlpatterns = [
    path('admin/', admin.site.urls),
    path('product_list', views.product_list, name='product_list'),          # Read all products
    path('product/<int:id>/', views.product_detail, name='product_detail'),  # Read a single product
    path('product/new/', views.product_create, name='product_create'),       # Create an product
    path('product/<int:id>/edit/', views.product_update, name='product_update'),  # Update an product
    path('product/<int:id>/delete/', views.product_delete, name='product_delete'), # Delete an product
    path('Shoppinglist/<int:id>/', views.Shoping_detail, name='Shopping_detail'),
    path('Shoppinglist/new/', views.Shopping_create, name='Shopping_create'),
    path('Shoppinglist/<int:id>/edit/', views.Shopping_update, name='Shopping_update'),
    path('Shoppinglist/<int:id>/delete/', views.Shopping_delete, name='Shopping_delete'),
    path('Shoppinglist', views.shopping_list, name='Shoppinglist'), 
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('', views.shopping_list, name='Shoppinglists'), 
]