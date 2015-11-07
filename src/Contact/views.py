from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
# Create your views here.

def contact(request):
	form_title = 'Contact Form'
	title = 'Contact Page'
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get('email')
		form_message = form.cleaned_data.get('message')
		form_full_name = form.cleaned_data.get('full_name')
		
		subject = 'Site Contact Form'
		from_email = settings.EMAIL_HOST_USER
		to_email = ['tarungupta.y12@lnmiit.ac.in', 'kii.tarung@gmail.com']
		contact_message = '%s: %s via %s' %(
				form_full_name,
				form_message,
				form_email)

		send_mail(subject,
				contact_message,
				from_email,
				to_email,
				fail_silently=False)

	context = {
		'title': title,
		'form_title': form_title,
		'form': form,
	}
	return render(request, 'forms.html', context)