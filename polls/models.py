from django.db import models
from django.utils import timezone
import datetime

class Questions(models.Model):
    question = models.CharField(max_length=200)
    time = models.DateTimeField('date published')

    def __str__(self):
        return self.question;

    def recent_questions(self):
        return self.time>=timezone.now()-datetime.timedelta(days=1);

class Choices(models.Model):
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice;

