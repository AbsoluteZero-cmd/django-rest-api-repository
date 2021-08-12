from django.db import models
from django.conf import settings
from questions.models import Question

class Answer(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	text = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)
	is_right = models.BooleanField(default=False)

	def __str__(self):
		return self.text

	class Meta:
		verbose_name = 'Answer'
		verbose_name_plural = 'Answers'
		ordering = ['-pub_date']