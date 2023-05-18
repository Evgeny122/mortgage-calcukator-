from django.db import models

class BankModel(models.Model):
    name_banks = models.CharField(max_length=20)
    term_min = models.IntegerField(default=0)
    term_max = models.IntegerField(default=0)
    rate_min = models.FloatField(default=0.0)
    rate_max = models.FloatField(default=0.0)
    payment_min = models.IntegerField(default=0)
    payment_max = models.IntegerField(default=0)

    def __str__(self):
        return self.name_banks