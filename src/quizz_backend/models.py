from django.db import models


# Create your models here.
class Quizz(models.Model):
    label = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now=True)


class QuizzItem(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    source_id = models.ForeignKey(to="QuizzAnswerSource", on_delete=models.DO_NOTHING)
    source_range = models.CharField(max_length=64)


class QuizzAnswerSource(models.Model):
    label = models.CharField(max_length=255)


class PupilLevel(models.Model):
    label = models.CharField(max_length=255)


class Pupil(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    level_id = models.ForeignKey(to="PupilLevel", on_delete=models.DO_NOTHING)
