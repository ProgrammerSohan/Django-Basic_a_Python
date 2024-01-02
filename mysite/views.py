from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse('<h3>Hello, This is Sohan</h3>');
    return render(request,"home.html")