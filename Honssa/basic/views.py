from django.shortcuts import render, redirect

def basic(request):
    return redirect('user:login')

# Create your views here.
