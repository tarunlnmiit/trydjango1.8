from django import forms

class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name

# IP CISCO 172.22.24.200