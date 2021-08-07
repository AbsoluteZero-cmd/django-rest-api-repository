from django import forms
from .models import Question


class QuestionSearchForm(forms.Form):
	search_field = forms.CharField(required=False)
	sort_field = forms.ChoiceField(choices=(('pub_date', 'By default'), ('id', 'ID'), ('pub_date', 'Published'), ('update_date', 'Updated'), ('title', 'Title'), ), required=False)
	sort_by = forms.ChoiceField(choices=(('-', 'Descending'), ('', 'Ascending')), )