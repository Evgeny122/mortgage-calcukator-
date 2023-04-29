from django.db import models

class BankModel(models.Model):
    name_banks = models.CharField(max_length=20)
    mortgage_rate = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.name_banks