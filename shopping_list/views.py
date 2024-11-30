from django.shortcuts import render, get_object_or_404 , redirect
from .models import Product, shoppinglist
from .forms import productform, Shoppingform
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



def product_list(request):
  product = Product.objects.all()
  return render(request, 'product_list.html',{'product': product})

def product_detail(request, id):
  product = get_object_or_404(Product, id=id)
  return render(request, 'product_detail.html',{'product': product}) 

def product_create(request):
  if request.method == 'POST':
    form = productform(request.POST)
    if form.is_valid():
      form.save()
      return redirect('product_list')
  else:
    form = productform()
  return render(request, 'product_form.html',{'form':form})  
  
def product_update(request, id):
  product = get_object_or_404(Product, id=id)
  if request.method == 'POST':
    form = productform(request.POST, instance=product)
    if form.is_valid():
      form.save()
      return redirect(product_list)
  else:
    form = productform(instance=product)
  return render(request,'product_form.html',{'form':form})
    
def product_delete(request, id):
  product = get_object_or_404(Product, id=id)
  if request.method == 'POST':
    product.delete()
    return redirect('product_list')
  return render(request, 'product_confirm.html', {"product": product})
  
def shopping_list(request):
  Shopping_list = shoppinglist.objects.filter(id_user=request.user).select_related('id_product')
  for item in Shopping_list:
    print(item.id_product.name)
  print(Shopping_list)
  context = {'shopping_list_items': Shopping_list}
  return render(request,'Shopping_list.html', context)

def Shoping_detail(request):
  Shoping_detail = get_object_or_404(shoppinglist, id_product=id, id_user=request.user)
  return render(request, 'Shoping_detail',{'Shoping_detail': Shoping_detail})

def Shopping_create(request):
  if request.method == 'POST':
     form = Shoppingform(request.POST, id_user=request.user)
     if form.is_valid():
      form.save()
      return redirect('Shoppinglist')
  else:
    form = Shoppingform(id_user=request.user)
    return render(request, 'Shopping_form.html',{'form': form})  
  
def Shopping_update(request, id):
  Shopping_update = get_object_or_404(shoppinglist, id_product=id, id_user=request.user)
  if request.method == 'POST':
    form = Shoppingform(request.POST, instance=Shopping_update)
    if form.is_valid():
      form.save()
      return redirect('Shoppinglist')
  else:
    form = Shoppingform(instance=Shopping_update)
  return render(request, 'Shopping_form.html', {'form': form})


def Shopping_delete(request, id):
  Shopping_delete = get_object_or_404(shoppinglist, id_product=id,id_user =request.user)
  if request.method == 'POST':
    Shopping_delete.delete()
    return redirect('Shoppinglist')
  return render(request, 'Shopping_confirm.html', {"Shopping_delete": Shopping_delete})

def login_view(request):
  if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user)
          return redirect('Shoppinglist')  
      else:
          messages.error(request, 'Invalid username or password')
  return render(request, 'log_in.html')


def logout_view(request):
  logout(request)
  messages.success(request, "You have been logged out successfully.")
  return redirect('login')  

def signup_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Your account has been created successfully. You can now log in.")
        return redirect('login')  # Redirect to the login page
  else:
    form = UserCreationForm()
  return render(request, 'signup.html',{'form':form})
