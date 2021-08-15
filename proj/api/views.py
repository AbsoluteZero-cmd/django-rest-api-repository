from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsAuthorOrStaffOrReadOnly
from api.serializers import QuestionSerializer
from questions.models import Question


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthorOrStaffOrReadOnly]
    filter_fields = ['title']
    search_fields = ['title', 'text']
    ordering_fields = ['update_date']

    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.save()
