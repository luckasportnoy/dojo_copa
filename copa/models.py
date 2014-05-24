from django.db import models

class Jogos(models.model):
	time1 = models.charfild(db_index=True, maxlength='50', null=False)
	time2 = models.charfild(db_index=True, maxlength='50', null=False)
	score1 = models.charfild(db_index=True, maxlength='50', null=False)
	score2 = models.charfild(db_index=True, maxlength='50', null=False)