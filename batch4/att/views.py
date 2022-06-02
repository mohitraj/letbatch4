from django.shortcuts import render
from .forms import StudentMasterForm
from django.shortcuts import render
from django.contrib import messages 

# Create your views here.

def StudentMaster(request):
	form = StudentMasterForm()
	context = {'form' : form}
	if request.method =='POST':
		form =  StudentMasterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f"Record added ")
		else:
			messages.warning(request,f"Error in the form")
	return render(request,"att/disform.html", context)