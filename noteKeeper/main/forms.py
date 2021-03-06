from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile, Notes, Papers
from datetime import datetime

class NotesForm(forms.ModelForm):
	sub_slug = forms.CharField(label = 'sub_slug', required = True)
	file_pdf = forms.FileField(label = 'file_pdf', required = True, widget=forms.ClearableFileInput(attrs={'multiple': True}))

	class Meta:
		model = Notes
		fields = ('file_published', 'sub_slug', 'file_pdf')

class PapersForm(forms.ModelForm):
	sem_slug = forms.CharField(label = 'sem_slug', required = True)
	file_pdf = forms.FileField(label = 'file_pdf', required = True, widget=forms.ClearableFileInput(attrs={'multiple': True}))

	class Meta:
		model = Papers
		fields = ('file_published', 'sem_slug', 'file_pdf')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'city', 'country']

class RegistrationForm(UserCreationForm):
	username = forms.CharField(label = 'username', required = True, max_length = 150)
	email = forms.EmailField(label = 'email', required = True)
	college = forms.CharField(label = 'college', max_length = 200)

	class Meta:
		model = User
		fields = ('username', 'college', 'email', 'password1', 'password2')

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		user.college = self.cleaned_data["college"]
		if commit:
			user.save()
		return user

	error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
        'usercheck': ("Username is already taken.")
	}
	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)
		return password2

	def clean_username(self):
		username = self.cleaned_data.get("username")
		if User.objects.filter(username=username):
			 raise forms.ValidationError(
				self.error_messages['usercheck'],
				code='usercheck',
			)
		return username

class LoginForm(AuthenticationForm):
	# email = forms.EmailField(required = False)

	class Meta:
		model = User
		fields = ('username', 'password')