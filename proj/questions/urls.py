from django.urls import path, include
from .views import QuestionList, QuestionDetail, QuestionCreate, QuestionEdit, QuestionDelete


app_name = 'questions'
urlpatterns = [
    path('question/<int:pk>/delete/', QuestionDelete.as_view(), name='delete'),
    path('question/<int:pk>/edit/', QuestionEdit.as_view(), name='edit'),
    path('question/<int:pk>/', QuestionDetail.as_view(), name='detail'),
    path('question/new/', QuestionCreate.as_view(), name='create'),
    path('', QuestionList.as_view(), name='list'),
]
