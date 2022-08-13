from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.
def register(request):

	if request.method=='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			user1 = form.cleaned_data.get("username")
			messages.success(request, f"Account is  created for {user1}")
			myProfile.objects.create(user=user1)
			return redirect("login")

	form = SignUpForm()
	context = {'form': form, 'legend' : "Register Today"}
	return render(request, 'users/login.html', context )