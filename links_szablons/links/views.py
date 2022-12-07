from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    return HttpResponse("text")

def url(request):
    return HttpResponse("Another text")

def fromFileHTML(request):
    template = loader.get_template('new.html')
    return HttpResponse(template.render())