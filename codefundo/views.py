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

    if request.method=="POST":
          form=input(request.POST)
         # mydate=request.POST.get("date",)
          cur_obj = form.save(commit=False)
          obj_track=track_users.objects.all()
          print(obj_track)
          for it in obj_track:
            print(it.pincode)
            if it.pincode == cur_obj.pincode:
              it.user_count=it.user_count + 1
              break
            else:
               it.pincode = cur_obj.pincode
               it.user_count=1
               it.save()
      
          for i in obj_track:
            print(i.pincode)
            print(i.user_count)
          print("manan")  
          if form.is_valid():
            cur_obj = form.save(commit=False)
            obj_track=track_users()
            obj_track.pincode = cur_obj.pincode
            obj_track.user_count
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