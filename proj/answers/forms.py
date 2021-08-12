from django import forms
from .models import Answer

class AnswerCreateForm(forms.ModelForm):

	class Meta:
		model = Answer
		fields = ['text', ] 


class AnswerIsRight(forms.Form):
	answer_id = forms.IntegerField()
	question_id = forms.IntegerField()
