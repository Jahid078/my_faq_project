#from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi
    question_bn = models.TextField(blank=True, null=True)  # Bengali

    def get_translated_question(self, lang):
        return getattr(self, f'question_{lang}', self.question)

    def __str__(self):
        return self.question
