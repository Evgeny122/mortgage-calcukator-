from django import forms
from .models import BankModel


class ClientForm(forms.Form):
    price = forms.IntegerField()
    contribution = forms.IntegerField()
    years = forms.IntegerField() 

class CreateBanksModelForm(forms.ModelForm):
    class Meta:
        model = BankModel
        exclude = []