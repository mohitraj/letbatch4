from django.shortcuts import render, redirect
from .forms import SignUp,UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.models import User
from .models import Profile as myprofile
from django.contrib.auth.decorators import login_required

# Create your views here.

def Register(request):
	form = SignUp()
	context = {"form": form, "legend" : "Register yourself"}
	if request.method =="POST":
		form = SignUp(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f"Account Created")
	return render(request,"user_app/disform.html", context)

@login_required(login_url="login")
def Profile(request):
	return render(request, 'user_app/profile.html')


def Profile_user(request, id1):
	u1 = User.objects.filter(id=id1)[0]
	context ={'user1': u1}
	return render(request, 'user_app/profile_user.html',context)

def loginpage(request):
	form = AuthenticationForm()
	context = {"form": form, "legend" : "Login"}

	next = ""
	if request.GET:
		next = request.GET['next']

	if request.method=='POST':
		form = AuthenticationForm(request=request,data= request.POST)
		print ("First********")
		if form.is_valid():
			print ("2nd********")
			username = request.POST.get("username")
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			print ("3rd********")
			if user is not None:
				login(request,user)  # session creation
				if next=="":
					return redirect('profile')
				else:
					return redirect(next)
			else:
				messages.warning(request,"Username and password is incorrect")


	return render(request,"user_app/disform.html", context)

@login_required(login_url="login")
def Updateprofile(request):
	try :
		if request.method =='POST':
			u_form = UserUpdateForm(request.POST,instance=request.user)
			p_form = ProfileUpdateForm(request.POST,request.FILES,instance= request.user.profile)
			if u_form.is_valid() and p_form.is_valid():
				u_form.save()
				p_form.save()
				messages.success(request,"Profile update")
				return redirect('profile')

		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance= request.user.profile)
		context = {'u_form': u_form, 'p_form': p_form, "legend": "Update Your profile"}

		return render(request, 'user_app/upprofile.html', context)

	except ValueError:
		myprofile.objects.create(user=request.user)

	except Exception as e :
			print (e)
			messages.warning(request,"Refresh Please ")
			myprofile.objects.create(user=request.user)
			#Profile.objects.create(user=request.user)

@login_required(login_url="login")
def user_change_pass(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			form = PasswordChangeForm(user=request.user,data= request.POST)
			if form.is_valid():
				form.save()
				update_session_auth_hash(request,form.user)
				messages.success(request,"password changed successfully")
				return redirect('profile')


	form = PasswordChangeForm(user= request.user)
	context = {'form': form, "legend":"Change password"}
	return render(request,'user_app/disform.html', context)

	
        

