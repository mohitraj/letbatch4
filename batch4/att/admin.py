from django.contrib import admin
from .models import MasterData 

@admin.register(MasterData)
class MasterAdmin(admin.ModelAdmin):
	list_display = ['stuid', 'stuname', 'stumail','subject']
	#list_display = __all__



# Register your models here.
