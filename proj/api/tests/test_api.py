# from django.contrib.auth.models import User
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
#
# from api.serializers import QuestionSerializer
# from questions.models import Question
#
#
# class QuestionApiTestCase(APITestCase):
#
#     def setUp(self):
#         self.user_1 = User.objects.create_user('Chevy Chase', 'chevy@chase.com', 'chevyspassword')
#         self.user_2 = User.objects.create_user('Jim Carrey', 'jim@carrey.com', 'jimspassword')
#         self.user_3 = User.objects.create_user('Dennis Leary', 'dennis@leary.com', 'denisspassword')
#
#         self.question1 = Question.objects.create(author=self.user_1, title='title 1', text='text 1')
#         self.question2 = Question.objects.create(author=self.user_2, title='title 2', text='text 5')
#         self.question3 = Question.objects.create(author=self.user_3, title='title 3', text='text 1')
#
#     def test_get(self):
#         url = reverse('question-list')
#         response = self.client_get(url)
#         serializer_data = QuestionSerializer([self.question1, self.question2, self.question3], many=True).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializer_data, response.data)
#
#
#
