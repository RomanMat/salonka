from django.shortcuts import redirect, render

from salon.forms import AddMaster, AddProduct, AddService
from .models import *

# Welcoming page for quick start / landing
def welcome(request):
    return render(request, 'salon/welcome.html')

# Hub page, where we will choose any ways ro administrate
def hub(request):
    return render(request, 'salon/hub.html')

# Masters listing edit page
def masters(request):
    profiles = Master.objects.all()
    return render(request, 'salon/masters.html', {'profiles': profiles})

# Services listing edit page
def services(request):
    services = Service.objects.all()
    return render(request, 'salon/services.html', {'services': services})

# Products listing edit page
def products(request):
    products = Product.objects.all()
    return render(request, 'salon/products.html', {'products': products})

# Page for user enter
def signin(request):
    return render(request, 'salon/signin.html')

# Page for registration user
def signup(request):
    return render(request, 'salon/signup.html')

# Info page about any successfull operation
def success(request):
    return render(request, 'salon/success.html')


###########################################################################3
# Adding master
def add_master(request):
    if request.method == 'POST':
        add_form = AddMaster(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('success')
    else:
        add_form = AddMaster()
    return render(request, 'salon/add_master.html', {'add_form': add_form})

# Adding service
def add_service(request):
    if request.method == 'POST':
        add_form = AddService(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('success')
    else:
        add_form = AddService()
    return render(request, 'salon/add_service.html', {'add_form': add_form})

# Adding product
def add_product(request):
    if request.method == 'POST':
        add_form = AddProduct(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('success')
    else:
        add_form = AddProduct()

    return render(request, 'salon/add_product.html', {'add_form': add_form})


def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('success')

def delete_master(request, id):
    master = Master.objects.get(id=id)
    master.delete()
    return redirect('success')

def delete_service(request, id):
    service = Service.objects.get(id=id)
    service.delete()
    return redirect('success')