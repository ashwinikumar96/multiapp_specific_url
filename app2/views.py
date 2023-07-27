from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def p3(request):
    return render(request,'p3.html')
def p4(request):
    return render(request,'p4.html')
def string(request):
    return HttpResponse('Hello World!!')