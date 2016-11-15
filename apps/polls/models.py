from django.db import models


class Question(models.Model):
    question_text = models.CharField('question text', max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField('choice text', max_length=200)
    votes = models.IntegerField('votes', default=0)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
