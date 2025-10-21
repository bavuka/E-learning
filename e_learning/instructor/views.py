from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import *
from django.contrib.auth.hashers import make_password

# Create your views here.
class InstructorRegView(View):
    def get(self,request):
        form=InstructorCreateForm()
        return render(request,"instructor_reg.html",{"form":form})
    def post(self,request):
         form=InstructorCreateForm(request.POST)
         if form.is_valid():
             res=form.save(commit=False)
            
             res.is_superuser=True
             res.is_staff=True
             res.role="instructor"
             res.password=make_password(form.cleaned_data.get("password"))
             print(res)
             print(form)
             res.save()
             return redirect("insreg")
             