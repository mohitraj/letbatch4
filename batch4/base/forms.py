from django import forms 

class StudentForm(forms.Form):
	UID = forms.IntegerField(label="UID")
	stuname = forms.CharField(max_length=100, label="NAME")
	stumail = forms.EmailField(max_length=100, label= "EMAIL")
	stuclass = forms.CharField(max_length=100, label= "Class")

