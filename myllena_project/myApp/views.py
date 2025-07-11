from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Bem vindo ao site da myllena!");
