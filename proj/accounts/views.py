from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from .forms import RegisterForm


from questions.models import Question

class NewLoginView(LoginView):
	template_name='accounts/login.html'

	def get_success_url(self):
		return reverse('questions:list')


class NewLogoutView(LogoutView):
	template_name='accounts/logout.html'
	next_page = reverse_lazy('questions:list')


class ProfileView(TemplateView):
	template_name = 'accounts/profile.html'

	def get_context_data(self, **kwargs):
		context = super(ProfileView, self).get_context_data(**kwargs)
		context['questions'] = Question.objects.filter(author=self.request.user)
		return context

class RegisterView(FormView):
	form_class = RegisterForm
	template_name = 'accounts/register.html'

	def form_valid(self, form):
		user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
		user.is_active = True
		user.save()
		login(self.request, user)
		return super(RegisterView, self).form_valid(form)

	def get_success_url(self):
		return reverse('questions:list')
	
