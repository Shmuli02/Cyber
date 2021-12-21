from django.db import models
from django import forms
from django.forms import ModelForm


from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
	
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	balance = models.IntegerField(User)
	dob = models.DateField(null=True,blank=True)

class Bike(models.Model):
	model = models.CharField(max_length=200)
	owner = models.IntegerField(User)
	status = models.IntegerField()



class Notes(models.Model):
	note = models.CharField(max_length=1000)
	bike = models.ForeignKey(Bike,on_delete=models.CASCADE)
	writer = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField(null=True,blank=True)

