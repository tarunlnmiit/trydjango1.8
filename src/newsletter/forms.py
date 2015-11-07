from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['email', 'firstname', 'lastname']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		# Additional email validation goes here
		return email

	def clean_firstname(self):
		firstname = self.cleaned_data.get('firstname')
		firstname = firstname.split()
		for name in firstname:
			if not name.isalpha():
				raise forms.ValidationError('Please enter a valid firstname')
		return ' '.join(firstname)

	def clean_lastname(self):
		lastname = self.cleaned_data.get('lastname')
		lastname = lastname.split()
		for name in lastname:
			if not name.isalpha():
				raise forms.ValidationError('Please enter a valid lastname')
		return ' '.join(lastname)

