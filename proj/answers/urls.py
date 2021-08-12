from django.urls import path, include
from . import views

app_name = 'answers'
urlpatterns = [
    path('', views.ans_is_right, name='is_right'),
]