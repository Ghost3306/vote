from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,"homepage.html")


def userl_login(request):


    
    return render(request,'user_login.html')


def admin_login(request):
    return render(request,'admin_login.html')

def register(request):
    return render(request,'register.html')

def crelection(request):
    return render(request,'crelection.html')

def search_election(request):
    return render(request,'search_election.html')