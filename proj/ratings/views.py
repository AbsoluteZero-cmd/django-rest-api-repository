from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Rating
from .forms import RatingCreateForm

from questions.models import Question

def add_rate(request):
	if request.method == 'POST':
		form = RatingCreateForm(request.POST)
		if form.is_valid():
			question_id = form.cleaned_data['question_id']
			rate = form.cleaned_data['rate']
			q = Question.objects.get(id=question_id)
			u = request.user
			rating = Rating(rate=rate, question=q, user=u)
			rating.save()
			return redirect(reverse('questions:detail', kwargs={'pk':q.pk}))

