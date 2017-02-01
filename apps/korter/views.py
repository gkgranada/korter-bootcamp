from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.

def default_view(request):
    return TemplateResponse(request, "korter/base.html", {})

def feed_view(request):
    return TemplateResponse(request, "korter/feed.html", {})

def neighbour_view(request):
    return TemplateResponse(request, "korter/neighbours.html", {}) 
