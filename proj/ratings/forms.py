from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms
from .models import Rating


class RatingCreateForm(forms.ModelForm):

	question_id = forms.IntegerField(widget=forms.HiddenInput)
	class Meta:
		model = Rating
		fields = ['rate', ]