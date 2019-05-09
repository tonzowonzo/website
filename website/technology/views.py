from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def technology(request):
    return HttpResponse("technology")