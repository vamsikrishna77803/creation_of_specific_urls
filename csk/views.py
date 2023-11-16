from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def dhoni(request):
    return render(request,'dhoni.html')
def raina(request):
    return HttpResponse('<h1>Mr.ipl</h1>')