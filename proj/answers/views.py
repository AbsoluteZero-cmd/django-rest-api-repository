from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


from questions.models import Question
from .models import Answer
from .forms import AnswerIsRight

def ans_is_right(request):
    if request.method == 'POST':
        form = AnswerIsRight(request.POST)
        if form.is_valid():
            answer_id = form.cleaned_data['answer_id']
            question_id = form.cleaned_data['question_id']
            q = Question.objects.get(id=question_id)
            a = Answer.objects.get(id=answer_id)
            a.is_right = True
            a.save()
            return redirect(reverse('questions:detail', kwargs={'pk':question_id}))