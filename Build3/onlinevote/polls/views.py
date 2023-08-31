from django.shortcuts import *
from .db import *
from .file import *
# Create your views here.
def homepage(request):
    return render(request,"homepage.html")


def userl_login(request):


    
    return render(request,'user_login.html')


def admin_login(request):
    if request.method=='POST':
        user_nm = request.POST.get('user')
        password = request.POST.get('passw')
        if verify(user_nm,password):
            return HttpResponseRedirect('crelection')
        else:
            return render(request,'admin_login.html',{'msgtype':'error','message':'Invalid Credintials'})
    return render(request,'admin_login.html')

def register(request):
    if request.method=='POST':
        typeuser = request.POST.get('type')
        crpass = request.POST.get('crpass')
        cnpass = request.POST.get('cnpass')

        email_u=request.POST.get('email')

        name = request.POST.get('fname')+' '+request.POST.get('mname')+' '+request.POST.get('lname')
        address_user = request.POST.get('address')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        org = request.POST.get('org')
        #have to calculate age before processing
        if crpass ==cnpass:
            if typeuser=='admin':
                if reg_admin(name,address_user,phone,email_u,'20',org,crpass):
                    return HttpResponseRedirect('adminlogin')
                else:
                    return render(request,'register.html',{'msgtype':'error','message':'Unexpected Error Occur'})
            elif typeuser=='user':
                pass
            else:
                return render(request,'register.html',{'msgtype':'error','message':'Please select User type!'})
        else:
            return render(request,'register.html',{'msgtype':'error','message':'Create and Confirm Password doesnt match'})
        


    return render(request,'register.html')
can_nm = []
def crelection(request):
    context={
        'gateway':'tab_cr'
    }
    if request.method=='POST':
        electiob_nm = request.POST.get('elec_tab')
        res = show_tab()
        for tab in  res:
            if electiob_nm == tab:
                context = {
                    'tab_cr':'error',
                    'message':'ELection name cannot be set'

                    }
                return render(request,'crelection.html',context)
        
        if type(electiob_nm)==str:
            
            print('table create sucess table: ' ,electiob_nm)
            write_tab(electiob_nm)
            if cr_election(electiob_nm):
                
                context = {
                    'title':'Admin Login',
                    'gateway':'comp_tab',
                    'table':electiob_nm
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
                        'table':electiob_nm,
                        'candidate' :can_nm
                    }
                return render(request,'admin.html',context)
   

    return render(request,'crelection.html',context)

def search_election(request):
    return render(request,'search_election.html')