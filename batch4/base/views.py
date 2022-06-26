from django.shortcuts import render
from django.http import HttpResponse 
from .forms  import StudentForm
from .models import Student
import json
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
'''
def live(request):
	return render(request, 'base/screen.html')

def screenfeed(request):
    return json.dumps([True, screenlive.gen()])
'''

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


def Student1(request):
	form = StudentForm()
	context = {"form": form, "legend": "Add your details"}

	if request.method=="POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			d1 = form.cleaned_data
			u1 = d1.get("UID")
			n1 = d1.get("stuname")
			m1 = d1.get("stumail")
			c1 = d1.get("stuclass")
			Student.objects.create(stuid=u1,stuname=n1,stumail=m1,stuclass=c1)
	
	return render(request,'base/simpleform.html', context )
