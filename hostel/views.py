from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from.models import UserProfile,Student,Post,Like,Order,Product
from .forms import StudentInfo, NewUserForm, OrderForm
from django.contrib import messages

# Authentication 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index(request):
    return render(request, 'home.html')

def Author(request):
    form = StudentInfo()

    if request.method == "POST":
        form = StudentInfo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')

    context = {
        "form": form,
    }   
    return render(request, "author.html", context=context)   

def Studentlist(request):
    student_list = Student.objects.all()

    context = {
        'students': student_list,
    } 
    return render(request, 'author-list.html', context=context)   

def register_request(request):
    form = NewUserForm()
    if request.method == "POST":
	    form = NewUserForm(request.POST)
	    if form.is_valid():
		    form.save()
		    messages.success(request, "Registration successful." )
		    return redirect('/')
    context = {
        'form': form
    }
    return render (request,"register.html", context=context)

    
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,"login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")    

#Food_Order
def food(request):
	products =Product.objects.all()
	cursor = {"products":products}
	return render(request,"food.html", cursor)

def products(request):
	return render(request, "products.html")

def order_list(request,pk):
    form = OrderForm()
    order_lists = Order.objects.get(id=pk)
    # product = order.product_id.name
    context = {"order": order_lists}
    return render(request, "order_list.html", context=context)


def createOrderForm(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order-list')
    context = {"form": form,}
    return render(request, 'order_form.html', context=context)

def updateOder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, 'order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {"item": order}
    return render(request, 'delete.html', context)	

