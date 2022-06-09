from django.shortcuts import render
from .forms import StudentMasterForm, StudentAttForm, StudentAttFormDisplay
from django.shortcuts import render
from django.contrib import messages 
import time 
from .models import Mark_Attendance2

# Create your views here.

def StudentMaster(request):
	form = StudentMasterForm()
	context = {'form' : form, 'legend' :" Register today"}
	if request.method =='POST':
		form =  StudentMasterForm(request.POST)
		if form.is_valid():
			mark1 =form.save(commit=False)
			form.save()
			messages.success(request,f"Record added ")
		else:
			messages.warning(request,f"Error in the form")
	return render(request,"att/disform.html", context)

def e_h(t1):
	t9=time.localtime(t1)
	return time.strftime("%d-%m-%Y-%H",t9)

def Mark_Att(request):
	form = StudentAttForm()
	context = {'form' : form, 'legend' :"Mark your Attendance"}
	try :
		if request.method=='POST':

			form = StudentAttForm(request.POST)
			if form.is_valid():
				print ("Hello ")
				mark1 =form.save(commit=False)
				mark1.time1 = int(time.time())
				mark1.ip_address = request.META.get('REMOTE_ADDR')
				mark1.platform = request.META.get('HTTP_USER_AGENT',"Unknown")
				mark1.date1 = e_h(mark1.time1)
				form.save()
				messages.success(request,f"{mark1.uid}, your Attendance is marked ")
			else:
				messages.warning(request,f"Error in the form")
	except Exception as e :
		messages.warning(request,f"{e}")
	return render(request,"att/disform.html", context)


def display_attendance(request):
	posts = Mark_Attendance2.objects.all()
	context = {"data": posts}
	return render(request,'att/displayallatt.html',context)


def display_attendanceone(request):
	form = StudentAttFormDisplay()
	context = {'form' : form}
	if request.method=='POST':
		form = StudentAttFormDisplay(request.POST)
		if form.is_valid():
			d1 = form.cleaned_data
			u1 = d1.get('UID')
			posts = Mark_Attendance2.objects.filter(uid=u1)
			context = {"data": posts}
			return render(request,'att/displayallatt.html',context)


	#posts = Mark_Attendance2.objects.all()
	#context = {"data": posts}
	return render(request,'att/disform.html',context)


