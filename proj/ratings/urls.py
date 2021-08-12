from django.urls import path, include
from . import views


app_name = 'ratings'
urlpatterns = [
    path('', views.add_rate, name='rating_form'),
]
