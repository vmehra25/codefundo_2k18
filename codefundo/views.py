from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import datetime
from django import template
from django.utils import timezone

from django.shortcuts import render,get_object_or_404
from codefundo.forms import input,Authentic,fund_gov
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from codefundo.models import user_details,gov_fund,track_users
from datetime import datetime,date,timedelta
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def main_page(request):
    form=input()
    #mypaste=user_details.objects.all()
    #mypaste = sorted(mypaste,key=lambda x:x.url,reverse=True)
    count_user=track_users()
    if request.method=="POST":
          form=input(request.POST)
         # myd
          current=form.save(commit=False)
          try:
             content_object=track_users.objects.get(pincode = current.pincode)
          except:
             content_object = None
          if content_object == None:
             content_object = track_users()
             content_object.pincode=current.pincode
             content_object.city=current.city
             
             content_object.user_count=1
             content_object.save()
          else :
              content_object.user_count=content_object.user_count+1
              content_object.save()
         
          
         
            
          if form.is_valid():
            
            form.save()
            return render(request,"codefundo/ss.html") 
          else:
               return render(request,"codefundo/return_valid_data.html")   
    return render(request,"codefundo/user_detail.html",{"form":form} )


def main_log_page(request):
    form=fund_gov()
    #mypaste=user_details.objects.all()
    #mypaste = sorted(mypaste,key=lambda x:x.url,reverse=True)
    sumq=0
    if request.method=="POST":
          form=fund_gov(request.POST)
         # mydate=request.POST.get("date",)
          if form.is_valid():
           # cur_obj = form.save(commit=False)
            form.save()
            item= gov_fund.objects.all()
            for i in item:
                 sumq=sumq+(int)(i.fund)
            print(sumq)
            form.save()
            return render(request,"codefundo/main_loggedin_page.html",{"sum":sumq}) 
            print("manan")
          else:
               return render(request,"codefundo/return_valid_data.html")   
    return render(request,"codefundo/main_loggedin_page.html",{"form":form } )



def user_signup(request):
    registered = False
    
    if request.method=="POST":
     auth=Authentic(request.POST )

     if auth.is_valid():
         auth=auth.save(commit=False)
         auth.set_password(auth.password)   
         #hashing the password
         auth.save()
         registered=True


     else :
         print("error")
    else:
        auth=Authentic()     
    return render(request,"codefundo/signup.html",{"auth":auth,"registered":registered })        


def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)


        if user:
            login(request,user)
            return HttpResponseRedirect(reverse("codefundo:main_log_page",))
        else:
            return render(request,"codefundo/return_invalid_user.html")
    else :
        return render(request,"codefundo/login.html",{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("codefundo:main_page",))