from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from new_one.models import Contact

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login/")
    return render(request, 'index.html')

def login_u(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html")
    return render(request, "login.html")

def logout_u(request):
    logout(request)
    return redirect("/login/")

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')
        Address = request.POST.get('Address')
        second_add = request.POST.get('second_add')
        contact = Contact(name=name, phone_number=phone_number, email=email, date_of_birth=date_of_birth, Address=Address, second_add=second_add)
        contact.save()
    return render(request, "create.html")


def singin(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        con_pass = request.POST["con_pass"]
        data = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        data.save()
        return redirect("/login/")
    return render(request, "singin.html")