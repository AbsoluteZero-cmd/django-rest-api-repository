from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.serializers import QuestionSerializer
from questions.models import Question


# class QuestionApiTestCase(APITestCase):
#
#     def setUp(self):
#         question1 = Question.objects.get(pk=1)
#         question2 = Question.objects.get(pk=2)
#         question3 = Question.objects.get(pk=3)
#
#     def test_get(self):
#         url = reverse('question-list')
#         response = self.client_get(url)
#         serializer_data = QuestionSerializer([self.question1, self.question2, self.question3], many=True).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializer_data, response.data)



