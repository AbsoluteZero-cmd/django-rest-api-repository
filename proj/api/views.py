from rest_framework.viewsets import ModelViewSet

from api.serializers import QuestionSerializer
from questions.models import Question


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
