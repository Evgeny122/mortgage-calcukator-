
from django.shortcuts import render, redirect
from .models import BankModel
from .forms import ClientForm, CreateBanksModelForm
from django.http import Http404


def form_calculator(request):
    obj_bank = BankModel.objects.all()
    form = ClientForm(request.POST or None)
    bank_offer = []
    
    # if form.is_valid():
    #     price = form.cleaned_data.get('price')
    #     contribution = form.cleaned_data.get('contribution')
    #     term = form.cleaned_data.get('term')
    
    if request.GET:
        price = int(request.GET['price'])
        contribution = int(request.GET['contribution'])
        term = int(request.GET['term'])
                
        for bank in obj_bank:
            if bank.term_min <= term <= bank.term_max:
                difference_term = bank.term_max - bank.term_min
                percent = ((term - bank.term_min)/difference_term) * 100
                decimal_form = percent/100
                difference_rate = bank.rate_max - bank.rate_min
                result_rate = (difference_rate * decimal_form) + bank.rate_min
                result_rate = round(result_rate, 2)
                monthly_payment = calculate_mortgage(price, contribution, term, result_rate)
                bank_offer_one = (bank.name_banks, result_rate, monthly_payment)
                bank_offer.append(bank_offer_one)
        return render(request, 'index.html', {'form' : form, 'bank_offer' : bank_offer})
    else:
        return render(request, 'index.html', {'form' : form, 'obj_bank' : obj_bank})

def calculate_mortgage(price, contribution, years, mortgage_rate):
    principal = price - contribution
    monthly_rate = mortgage_rate / 1200
    months = years * 12
    monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    return round(monthly_payment, 2)

def calculate_mortgage(price, contribution, years, mortgage_rate):
    principal = price - contribution
    monthly_rate = mortgage_rate / 1200
    months = years * 12
    monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    return round(monthly_payment, 2)

def create_banks(request):
    form = CreateBanksModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect('/')
    return render(request, 'create_bank_form.html', {'form' : form})

def edit_bank(request, pk):
    try:
        obj = BankModel.objects.get(id=pk)
    except BankModel.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = CreateBanksModelForm(request.POST, instance=obj)
        if form.is_valid():
            edit_obj = form.save(commit=False)
            edit_obj.save()
            return redirect('/')
    else:
        form = CreateBanksModelForm(instance=obj)
        return render(request, 'edit_bank_form.html', {'form' : form, 'single_obj' : obj})


def delete(request, pk):
    try:
        obj = BankModel.objects.get(id=pk)
    except BankModel.DoesNotExist:
        raise Http404
    obj.delete()
    return redirect('/')