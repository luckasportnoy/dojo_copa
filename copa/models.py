from django.db import models

class Jogos(models.Model):
  score1 = models.CharField(max_length='50', null=False)
  score2 = models.CharField(max_length='50', null=False)
  score3 = models.CharField(max_length='50', null=False)
  score4 = models.CharField(max_length='50', null=False)
  score5 = models.CharField(max_length='50', null=False)
  score6 = models.CharField(max_length='50', null=False)