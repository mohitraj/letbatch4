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

class MasterData1(models.Model):
	class Meta:
		unique_together = (('stuid','subject'),)

	stuid = models.IntegerField()
	stuid_sub = models.CharField(unique=True, max_length=100)
	stuname = models.CharField(max_length=100)
	stumail = models.EmailField(max_length=100)
	subject = models.CharField(max_length=100)

	def __str__(self):
		return str(self.stuid)



class Mark_Attendance(models.Model):
	class Meta:
		unique_together = (('uid','date1'),('date1','ip_address'))
	uid = models.ForeignKey('MasterData1',related_name="uid", to_field='stuid_sub', on_delete=models.CASCADE)
	subject_name = models.CharField(max_length=100)
	time1 = models.IntegerField(null=False)
	ip_address = models.CharField(max_length=100, null=False)
	date1 = models.CharField(max_length=100,null=False)
	platform = models.CharField(max_length=200, null= False)

	def __str__(self):
		return str(self.id)


class MasterData2(models.Model):
	stuid = models.IntegerField(unique=True, null=False)
	stuname = models.CharField(max_length=100)
	stumail = models.EmailField(max_length=100)
	

	def __str__(self):
		return str(self.stuid)



class Mark_Attendance2(models.Model):
	class Meta:
		unique_together = (('uid','date1'),('date1','ip_address'))
	uid = models.ForeignKey('MasterData2',related_name="uid", to_field='stuid', on_delete=models.CASCADE)
	subject_name = models.CharField(max_length=100)
	time1 = models.IntegerField(null=False)
	ip_address = models.CharField(max_length=100, null=False)
	date1 = models.CharField(max_length=100,null=False)
	platform = models.CharField(max_length=200, null= False)

	def __str__(self):
		return str(self.id)

# Create your models here.
