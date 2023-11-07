from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jampandu(request):
    return HttpResponse('<h1><marquee>hlo babisha</h1></marquee>')
def kannayya(request):
    return HttpResponse('kesiho sakhi sukh meh tu hu')