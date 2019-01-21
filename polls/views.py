from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello world, you are at the poll index")

def test(request):
	return HttpResponse("This is for testing")

# Create your views here.
