from django import forms
from .models import links


class UrlForm(forms.ModelForm):
	class Meta:
		model = links
		fields = ['url']
