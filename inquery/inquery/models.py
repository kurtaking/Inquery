from django.db import models
from django.contrib.auth.models import User as AuthUser

class Question(models.Model):
    question = models.CharField(max_length=200)


class Answer(models.Model):
    answer = models.CharField(max_length=1000)


class FlashCard(models.Model):
    question = models.ManyToManyField(Question)
    answer = models.ManyToManyField(Answer)


class Category(models.Model):
    name = models.CharField(max_length=100)
    flash_cards = models.ManyToManyField(FlashCard)


class User(AuthUser):
    categories = models.ManyToManyField(Category)

