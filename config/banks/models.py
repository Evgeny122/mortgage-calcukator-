from django.db import models

class BankModel(models.Model):
    name_banks = models.CharField(max_length=20)
    mortgage_rate = models.FloatField(default=0.0)
    payment = models.IntegerField(default=0)