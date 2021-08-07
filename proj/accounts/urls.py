from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import NewLoginView, NewLogoutView, ProfileView, RegisterView


app_name = 'accounts'
urlpatterns = [
    path('profile/', login_required(ProfileView.as_view()), name='profile'),
    path('logout/', login_required(NewLogoutView.as_view()), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', NewLoginView.as_view(), name='login'),
]
