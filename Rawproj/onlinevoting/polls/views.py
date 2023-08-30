from django.shortcuts import render
from django.http import *
from .db import *
from polls import *
from .file import *
# Create your views here.
def launch(request):
    write_file("notverified")
    if request.method == 'POST':
        user=request.POST.get('user')
        passw=request.POST.get('pass')
        print(user,passw)
        if verify(user,passw):
            write_file("verified")
            return HttpResponseRedirect("home")
    return render(request,"Login.html")

def home(request):
    if read_file():
        data={  
            'var':'Shivani Malkar',
            'users':["Cheyenne Coutinho","Rufus Ajgaonkar","Lalit Rawool","Siddhi Adulkar"]
        }
        return render(request,'home_page.html',data)
    return HttpResponseRedirect("")
def register(request):
    
    return render(request,'reg.html')

can_nm = []

def admin(request):

    context = {
        'title':'Admin Login',
        'gateway':'tab_cr'
    }
    if request.method == 'POST':
        cr_tab  =  request.POST.get('elec_tab')
        if type(cr_tab)==str:
            
            print('table create sucess table: ' ,cr_tab)
            write_tab(cr_tab)
            if cr_election(cr_tab):
                
                context = {
                    'title':'Admin Login',
                    'gateway':'comp_tab',
                    'table':cr_tab
                }
                return render(request,'admin.html',context)
        
        
        can_name = request.POST.get('can_nm')
        if type(can_name)==str:
            table_name = read_tab()
            if insert_tab(table_name,can_name):

                can_nm.append(can_name)
                print('candidate name is :',can_name)
                context = {
                        'title':'Admin Login',
                        'gateway':'comp_tab',
                        'table':cr_tab,
                        'candidate' :can_nm
                    }
                return render(request,'admin.html',context)
    return render(request,'admin.html',context)