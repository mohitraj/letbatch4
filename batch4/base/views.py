from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def about(request):
	#print (request)
	#print (request.META.keys())
	print (request.META['HTTP_USER_AGENT'])
	print (request.META['REMOTE_ADDR'])
	return HttpResponse("<h1> Hello Everyone </h1>")


def hello(request):
	return HttpResponse("<h1> My second hello </h1>")

def ok(request):
	return HttpResponse("<h1> ok </h1>")