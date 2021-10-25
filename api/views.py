from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def form(request):
    return HttpResponse('<h1>Hello</h1>')

def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/registration')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('/dashboard')
        else:
             messages.info(request,'Password Taken')
        return redirect('/registration')

    else:
        return render(request, 'registration.html')
    
def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/login')
    else:
        return render(request, 'hello.html')

def logout(request):
    auth.logout(request)
    return redirect('/login')

def index(request):
    return render(request, 'index.html')

def courses(request):
    return render(request, 'courses.html')

def about(request):
    return render(request, 'about.html')

def trainers(request):
    return render(request, 'trainers.html')

def events(request):
    return render(request, 'events.html')

def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    return render(request, 'contact.html')

def courseDetails(request):
    return render(request, 'course-details.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def user(request):
    return render(request, 'user.html')

def admindashboard(request):
    return render(request, 'admindashboard.html')

def viewquestions(request):
    return render(request, 'view_question.html')

def questionsetupload(request):
    return render(request, 'questionsetupload.html')

def questionpanel(request):
    return render(request, 'questionpanel.html')

def createquestions(request):
    return render(request, 'createquestions.html')

