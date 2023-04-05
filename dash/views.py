from django.shortcuts import render
from .models import *
# Create your views here.
def Home1(request):
    context=Home.objects.all()
    return render (request,'dash/home.html',{'context':context})