from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm

class Staff_NIDForm(ModelForm):

	class Meta:
		model = Staff_NID
		fields = ('NID', 'HeadquartersID',)

class NewUserForm(UserCreationForm):
	firstname = forms.CharField(required=True)
	lastname = forms.CharField(required=True)

	class Meta:
		model = User
		fields = ("firstname", "lastname", "username", "password1", "password2")

	def __init__(self, *args, **kwargs):
		super(NewUserForm, self).__init__(*args, **kwargs)

		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.firstname = self.cleaned_data['firstname']
		user.firstname = self.cleaned_data['lastname']
		if commit:
			user.save()
		return user