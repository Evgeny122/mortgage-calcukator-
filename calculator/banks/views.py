from django.shortcuts import render, redirect
from .models import BankModel
from .forms import ClientForm

def form_calculator(request):
    obj_bank = BankModel.objects.all()
    form = ClientForm(request.POST or None)
    bank_offer = []
    if form.is_valid():
        price = form.cleaned_data.get('price')
        contribution = form.cleaned_data.get('contribution')
        years = form.cleaned_data.get('years')
        for bank in obj_bank:
            monthly_payment = calculate_mortgage(price, contribution, years, bank.mortgage_rate)
            bank_offer_one = (bank.name_banks, bank.mortgage_rate, monthly_payment)
            bank_offer.append(bank_offer_one)
        return render(request, 'index.html', {'form' : form, 'bank_offer' : bank_offer})
    return render(request, 'index.html', {'form' : form})

def calculate_mortgage(price, contribution, years, mortgage_rate):
    principal = price - contribution
    monthly_rate = mortgage_rate / 1200
    months = years * 12
    monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    return round(monthly_payment, 2)

# def count_mortgage(request):
#     obj_bank = BankModel.objects.all()
#     bank_offer = []
#     form = ClientForm(request.POST)
#     if form.is_valid():
#         price = form.cleaned_data.get('price')
#         contribution = form.cleaned_data.get('contribution')
#         years = form.cleaned_data.get('years')
#         for bank in obj_bank:
#             monthly_payment = calculate_mortgage(price, contribution, years, bank.mortgage_rate)
#             bank_offer_one = (bank.name_banks, bank.mortgage_rate, monthly_payment)
#             bank_offer.append(bank_offer_one)
#         return render(request, 'index.html', {'form' : form, 'bank_offer' : bank_offer})
    

