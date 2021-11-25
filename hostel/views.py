from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from.models import UserProfile,Student,Post,Like
from .forms import StudentInfo, NewUserForm
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
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request,"register.html", context={"register_form":form})

    
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