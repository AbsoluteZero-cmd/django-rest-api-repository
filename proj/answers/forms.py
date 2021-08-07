from django import forms
from .models import Answer

class CreateAnswerForm(forms.ModelForm):

	class Meta:
		model = Answer
		fields = ['text', ]