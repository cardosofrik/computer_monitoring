
from django.db import models
from django.contrib.auth.models import User
class TabelaEnd(models.Model):
    ip = models.CharField(max_length=120, null=False)
    porta = models.CharField(max_length=120, null=False)
    nome =  models.CharField(max_length=120, null=False)
    aparelho = models.CharField(max_length=50, null=False)
    usuario = models.ForeignKey(User, models.CASCADE,  related_name="TabelaEnd")
