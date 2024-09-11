from rest_framework import viewsets

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is the donation website")
