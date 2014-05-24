from django.db import models

class Jogos(models.Model):
	time1 = models.CharField(db_index=True, max_length='50', null=False)
	time2 = models.CharField(db_index=True, max_length='50', null=False)
	score1 = models.CharField(db_index=True, max_length='50', null=False)
	score2 = models.CharField(db_index=True, max_length='50', null=False)