from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import QuestionSearchForm
from .models import Question

from answers.models import Answer
from answers.forms import AnswerCreateForm

from ratings.models import Rating
from ratings.forms import RatingCreateForm


class QuestionList(ListView):
	model = Question
	template_name = 'questions/list.html'
	context_object_name = 'questions'
	paginate_by = 5

	def dispatch(self, request, *args, **kwargs):
		self.search_form = QuestionSearchForm(request.GET)
		self.search_form.is_valid()
		return super(QuestionList, self).dispatch(request, *args, **kwargs)

	def get_queryset(self):
		queryset = super(QuestionList, self).get_queryset()
		search_field = self.search_form.cleaned_data.get('search_field')
		sort_field = self.search_form.cleaned_data.get('sort_field')
		sort_by = self.search_form.cleaned_data.get('sort_by')

		if search_field:
			queryset = queryset.filter(title__icontains=search_field)
		if sort_field:
			queryset = queryset.order_by(sort_field)
			if sort_by:
				queryset = queryset.order_by(sort_by + sort_field)
		return queryset

	def get_context_data(self):
		context = super(QuestionList, self).get_context_data()
		context['search_form'] = self.search_form
		return context


class QuestionDetail(DetailView):
	model = Question
	template_name = 'questions/detail.html'
	context_object_name = 'question'

	def dispatch(self, request, *args, **kwargs):
		self.answers = Answer.objects.filter(question=self.get_object())
		try:
		    self.rate = Rating.objects.get(question=self.get_object(), user=self.request.user)
		except Rating.DoesNotExist:
		    self.rate = None
		return super(QuestionDetail, self).dispatch(request, *args, **kwargs)

	# Handle POST GTTP requests
	def post(self, request, *args, **kwargs):
		form = AnswerCreateForm(request.POST)
		if form.is_valid():
			new_answer = form.save(commit=False)
			new_answer.author = request.user
			new_answer.question = self.get_object()
			new_answer.save()
			return redirect('questions:detail', pk=self.get_object().pk)

	def get_queryset(self):
		queryset = super(QuestionDetail, self).get_queryset()
		return queryset

	def get_context_data(self, **kwargs):
		context = super(QuestionDetail, self).get_context_data(**kwargs)
		context['form'] = AnswerCreateForm()
		context['answers'] = self.answers
		context['rate'] = self.rate
		context['rating_form'] = RatingCreateForm()
		return context


class QuestionCreate(CreateView):
	model = Question
	template_name = 'questions/create.html'
	fields = ['title', 'text']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(QuestionCreate, self).form_valid(form)

	def get_success_url(self):
		return reverse('questions:detail', kwargs={'pk': self.object.pk})


class QuestionEdit(UpdateView):
	model = Question
	template_name = 'questions/edit.html'
	fields = ['title', 'text']

	def get_success_url(self):
		return reverse('questions:detail', kwargs={'pk': self.object.pk})


class QuestionDelete(DeleteView):
	model = Question
	template_name = 'questions/delete.html'
	context_object_name = 'question'

	def get_success_url(self):
		return reverse('questions:list')