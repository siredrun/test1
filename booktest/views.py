from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader

# Create your views here.

def index(request):
    temp = loader.get_template('index.html')
    return HttpResponse(temp.render())