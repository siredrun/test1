from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
from .models import *

# Create your views here.

def index(request):
    blist= BookInfo.objects.all()
    context = {'list':blist}
    return render(request, 'booktest/index.html',context)
def show(request, id):
    alist = BookInfo.objects.get(pk=id)
    book = alist.heroinfo_set.all()
    context = {'list':book}
    return render(request, 'booktest/show.html',context)