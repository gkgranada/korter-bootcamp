from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.

def default_view(request):
    return TemplateResponse(request, "korter/base.html", {})

def feed_view(request):
    return TemplateResponse(request, "korter/feed.html", {})

def feedManage_view(request):
    return TemplateResponse(request, "korter/feedManage.html", {})

def bill_view(request):
    return TemplateResponse(request, "korter/bills.html", {})

def neighbours_view(request):
    return TemplateResponse(request, "korter/neighbours.html", {})

def documents_view(request):
    return TemplateResponse(request, "korter/documents.html", {})

def account_view(request):
    return TemplateResponse(request, "korter/account.html", {})
