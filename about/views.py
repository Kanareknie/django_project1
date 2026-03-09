from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about_request(request):
    return HttpResponse("Hello, Abount!")
# Create your views here.
