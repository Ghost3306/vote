from pyexpat.errors import messages
from django.http import JsonResponse
from django.shortcuts import *
from .db import *
from .file import *
import json
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
                user_status(user_nm)
                write_login(user_nm)
                return HttpResponseRedirect('search_election')
            else:
                data = {
                    'messages':'Invalid Username or password'
                }
                messages.success(request, 'Invalid Username or password') 
               
                
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
                        
                        
                        return HttpResponseRedirect('userlogin')
                    else:
                        return render(request,'register.html',{'msgtype':'error','message':'Unexpected Error Occur'})
                elif typeuser=='user':
                    if reg_user(name,email_u,phone,'20',address_user,'user',crpass):
                        return HttpResponseRedirect('userlogin')
                    else:
                        return render(request,'register.html',{'msgtype':'error','message':'Unexpected Error Occur'})
                else:
                    return render(request,'register.html',{'msgtype':'error','message':'Please select User type!'})
            else:
                return render(request,'register.html',{'msgtype':'error','message':'Create and Confirm Password doesnt match'})
        


    return render(request,'register.html')

tab_nm =""
can_nm = []
def crelection(request):
    li_tab = get_elec_list()
    context={
        'gateway':'tab_cr',
        'table_list':li_tab
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
                        'table':electiob_nm,
                        'table_list':li_tab
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
                        'candidate' :can_nm,
                        'table_list':li_tab
                    }
                tab_nm=table_name
                return render(request,'crelection.html',context)
            
   
    return render(request,'crelection.html',context)

def search_election(request):
    if request.method=='POST':
        campaign_name = request.POST.get('campaign')
        if type(campaign_name) == str:
            user = read_login()
            res = search_user(user,campaign_name)
            if res=='false':
                return HttpResponse("You Alredy Vote this campaign")
            else:
                det = ""
                for x in campaign_name:
                    if x =='_':
                        break
                    else:
                        det += x
                write_cam(det)
                table_data = show_cam(det)
                data = {
                    'table':table_data
                }
                return render(request,'search_election.html',data)
    
    vote_nm = request.POST.get('status')
    tab_name = read_cam()
    if type(vote_nm)==str:
        if fil_vote(vote_nm,tab_name):
            return HttpResponseRedirect('msg')
        else:
            return HttpResponse("Error")
    return render(request,'search_election.html')

    
def submit(request):
    data = {
        'tab':read_tab(),
        'uid':get_uid(read_tab())
    }
    
    return render(request,'submit.html',data)

def msg(request):
    return render(request,'msg.html')