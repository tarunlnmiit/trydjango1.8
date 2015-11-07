from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.

def home(request):
	title = 'Welcome'
	# if request.user.is_authenticated():
	# 	title = 'Hello there, %s ' %(request.user)
	
	form = SignUpForm(request.POST or None)

	context = {
		'title': title,
		'form': form
	}

	if form.is_valid():
		instance = form.save(commit=False)
		lastname = form.cleaned_data.get('lastname')
		if not lastname:
			lastname = 'Mitch'
		instance.lastname = lastname
		# if not instance.lastname:
		# 	instance.lastname = 'Mitch'
		instance.save()
		context = {
			'title': 'Thank You'
		}

	return render(request, 'home.html', context)

