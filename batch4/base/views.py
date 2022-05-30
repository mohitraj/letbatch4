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
	
	context = {"name" : "ravinder", "title": "Batch 4"}
	return render(request, 'base/about.html', context)

def ok(request):
	posts =  [
	{
	"author" : "Mohit", 	"title" : "Post1",
	"content" : "Hello everyone this is my first post "
	},
		{
	"author" : "ravinder",
	"title" : "Post2",
	"content" : "Hello everyone this is my first post "
	}
	]
	context = {"posts" : posts, }
	return render(request, "base/data.html", context )

def home(request):
	return render(request, 'base/base.html')

def ravinder(request):
	list1 = ["Thor", "ironman", "captain"]
	return render (request, 'base/heros.html', {"avengers": list1})