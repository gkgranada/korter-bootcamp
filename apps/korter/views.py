from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.

def default_view(request):
    return TemplateResponse(request, "korter/base.html", {})

def feed_view(request):
    return TemplateResponse(request, "korter/feed.html", {})

def rules_view(request):
    return TemplateResponse(request, "korter/rules.html", {})

def neighbour_view(request):
    return TemplateResponse(request, "korter/neighbours.html", {})

def contract_view(request):
    return TemplateResponse(request, "korter/contract.html", {})

def bill_view(request):
    return TemplateResponse(request, "korter/bills.html", {})

def rules_view(request):
    return TemplateResponse(request, "korter/rules.html", {})

def account_view(request):
    return TemplateResponse(request, "korter/account.html", {})
