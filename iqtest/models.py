from django.db import models
from django_quill.fields import QuillField
from accounts.models import Profile
from django.core.validators import MaxValueValidator

# Create your models here.

class Question(models.Model):
    question = QuillField(blank=False)

class Choice(models.Model):
    class answerTextChoices(models.TextChoices):
        CORRECT = 'correct', 'Correct'
        INCORRECT = 'incorrect', 'Incorrect'
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    choice = QuillField()
    is_answer = models.CharField(max_length=32, choices=answerTextChoices.choices, blank=False, default=answerTextChoices.INCORRECT)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, blank=True)
    result = models.ForeignKey('Result', on_delete=models.SET_NULL, null=True, blank=True)
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name="iq_answer_user")


class Result(models.Model):
        
    class labelTextChoices(models.TextChoices):
        EXCEPTIONAL = 'exceptional', 'Exceptional'
        EXCELLENT = 'excellent', 'Excellent'
        VERYGOOD = 'verygood', 'Very Good'
        GOOD = 'good', 'Good'
        AVERAGE = 'average', 'Average'

    @property
    def get_label(self):
        if self.result in range(36,41):
            return self.labelTextChoices.EXCEPTIONAL
        elif self.result in range(30, 36):
            return self.labelTextChoices.EXCELLENT
        elif self.result in range(25,31):
            return self.labelTextChoices.VERYGOOD
        elif self.result in range(20,26):
            return self.labelTextChoices.VERYGOOD
        return self.labelTextChoices.AVERAGE
    
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="iq_result")
    result = models.IntegerField(blank=False, validators=[MaxValueValidator(100)])
    date_created = models.DateTimeField(auto_now_add=True)

