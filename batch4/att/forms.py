from .models import MasterData2, Mark_Attendance2
from django import forms 


class StudentMasterForm(forms.ModelForm):
	class Meta :
		model = MasterData2
		fields = ["stuid", "stuname", "stumail"]


class StudentAttForm(forms.ModelForm):
	class Meta:
		model = Mark_Attendance2
		fields = ['uid','subject_name']

class StudentAttFormDisplay(forms.Form):
	UID = forms.IntegerField(label="UID")
	