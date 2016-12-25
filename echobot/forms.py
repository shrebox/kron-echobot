from django.forms import ModelForm
from django.db import models
from django import forms

class Name(models.Model):
	input_text = models.CharField(max_length=100)
	def __str__(self):
		return self.input_text
		
class NameForm(ModelForm):
	class Meta:
		model= Name
		fields = ['input_text']