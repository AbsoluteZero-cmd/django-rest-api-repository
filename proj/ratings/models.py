from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from questions.models import Question

class Rating(models.Model):
	rate = models.PositiveSmallIntegerField(default=1, choices=[(i, str(i)) for i in range(1, 11)])
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return '{} rate'.format(self.question)

	class Meta:
		# а вот эта команда и не даст повторно голосовать
		unique_together = ('user', 'question')