from .models import MasterData
from django import forms 


class StudentMasterForm(forms.ModelForm):
	class Meta :
		model = MasterData
		fields = ["stuid", "stuname", "stumail","subject"]