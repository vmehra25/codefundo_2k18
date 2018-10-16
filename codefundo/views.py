from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import datetime
from django import template
from django.utils import timezone

from django.shortcuts import render,get_object_or_404
from codefundo.forms import input
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from codefundo.models import user_details
from datetime import datetime,date,timedelta
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def main_page(request):
    form=input()
    #mypaste=user_details.objects.all()
    #mypaste = sorted(mypaste,key=lambda x:x.url,reverse=True)

    if request.method=="POST":
          form=input(request.POST)
         # mydate=request.POST.get("date",)
          if form.is_valid():
            form.save()
            
            return render(request,"codefundo/ss.html") 
          else:
               return render(request,"codefundo/return_valid_data.html")   
    return render(request,"codefundo/user_detail.html",{"form":form } )