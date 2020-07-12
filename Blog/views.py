from django.shortcuts import render

# Create your views here.
from Blog.models import Python, Java, Csharp, Html


def home(request):
    return render(request,'index.html')


def python(request):
    data = Python.objects.all()
    return render(request, 'python.html',{'data':data})


def java(request):
    data = Java.objects.all()
    return render(request, 'java.html',{'data':data})


def csharp(request):
    data = Csharp.objects.all()
    return render(request, 'csharp.html',{'data':data})


def html(request):
    data = Html.objects.all()
    return render(request, 'hypertext.html',{'data':data})