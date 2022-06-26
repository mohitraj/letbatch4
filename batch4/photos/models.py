from django.db import models


class PhotoGallary(models.Model):
	multipleimages = models.FileField(upload_to="galleries",blank=True,null=True)
# Create your models here.
