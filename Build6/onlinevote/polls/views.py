from django.shortcuts import *
from .db import *
from .file import *
# Create your views here.
def homepage(request):
    return render(request,"homepage.html")


def login(request):
    if request.method=='POST':
        user_nm = request.POST.get('user')
        password = request.POST.get('passw')
        if type(user_nm)==str:
            res = verify(user_nm,password)
            print(res)
            if res=='admin':
                write_login(user_nm)
                return HttpResponseRedirect('crelection')
            elif res =='user':
                write_login(user_nm)
                return HttpResponseRedirect('search_election')
            else:
                return render(request,'user_login.html',{'msgtype':'error','message':'Invalid Credintials'})
    return render(request,'user_login.html')

    
    




def register(request):
    if request.method=='POST':

        typeuser = request.POST.get('type')
        crpass = request.POST.get('crpass')
        cnpass = request.POST.get('cnpass')

        email_u=request.POST.get('email')

        name = request.POST.get('fname')+' '+request.POST.get('mname')+' '+request.POST.get('lname')
        address_user = request.POST.get('address')
        phone = request.POST.get('phone')
        
        
        if type(name)==str and type(crpass)==str:

        #have to calculate age before processing
            if crpass ==cnpass:
                if typeuser=='admin':
                    if reg_admin(name,email_u,phone,'20',address_user,'admin',crpass):
                        
                        
                        return HttpResponseRedirect('adminlogin')
                    else:
                        return render(request,'register.html',{'msgtype':'error','message':'Unexpected Error Occur'})
                elif typeuser=='user':
                    if reg_user(name,email_u,phone,'20',address_user,'user',crpass):
                        return HttpResponseRedirect('adminlogin')
                    else:
                        return render(request,'register.html',{'msgtype':'error','message':'Unexpected Error Occur'})
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
        if type(electiob_nm)==str:
            print('selected name for election :',electiob_nm)
            res = tab_selection(electiob_nm)
            write_tab(electiob_nm)
            if res!=False:
                print('table create sucess table: ' ,electiob_nm)   
                if cr_election(electiob_nm):
                    can_nm.clear()  
                    context = {
                        'title':'Admin Login',
                        'gateway':'comp_tab',
                        'table':electiob_nm
                    }
                    return render(request,'crelection.html',context) 
            else:
                context = {
                        'tab_cr':'error',
                        'message':'Election name cannot be set'

                        }
                return render(request,'crelection.html',context)
            
        can_name = request.POST.get('can_nm')
        table_name = read_tab()
        if type(can_name)==str:
            if insert_tab(table_name,can_name):

                can_nm.append(can_name)
                print('candidate name is :',can_name)
                context = {
                        'title':'Admin Login',
                        'gateway':'comp_tab',
                        'table':table_name,
                        'candidate' :can_nm
                    }
                return render(request,'crelection.html',context)
            
   
    return render(request,'crelection.html',context)

def search_election(request):
    return render(request,'search_election.html')