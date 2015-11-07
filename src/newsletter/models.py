from django.db import models

# Create your models here.

class SignUp(models.Model):
	email = models.EmailField()
	firstname = models.CharField(max_length=20, blank=False, null=False)
	lastname = models.CharField(max_length=20, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.email