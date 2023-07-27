from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def p5(request):
    return render(request,'p5.html')
def p6(request):
    return render(request,'p6.html')
def string(request):
    return HttpResponse('Hello World!!')