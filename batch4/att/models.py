from django.db import models


class MasterData(models.Model):
	class Meta:
		unique_together = (('stuid','subject'),)
	stuid = models.IntegerField()
	stuname = models.CharField(max_length=100)
	stumail = models.EmailField(max_length=100)
	subject = models.CharField(max_length=100)

	def __str__(self):
		return str(self.stuid)


class Mark_Attendance(models.Model):
	
# Create your models here.
