from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	email = models.EmailField(_('email address'), unique = True)
	native_name = models.CharField(max_length = 5)
	phone_no = models.CharField(max_length = 10)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
	
	def __str__(self):
		return "{}".format(self.email)
