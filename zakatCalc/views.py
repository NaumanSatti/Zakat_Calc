from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from bs4 import BeautifulSoup
import requests
from .forms import ZakatForm
def get_price(url,x,classs):
    page= requests.get(url)


    Soup= BeautifulSoup(page.content, 'html.parser')
    info=Soup.find_all(class_=classs)
    count=0
    
    for items in info:
      count+=1
      if(count==x):
        data=items.get_text()
    
    gold=float(data.replace(',', ''))
    return gold

def index(request):
    
    
    a=23
    gold=get_price("https://www.livepriceofgold.com/pakistan-gold-price.html",29,"bold3")
    page= requests.get("https://hamariweb.com/finance/silver_rate/")


    Soup= BeautifulSoup(page.content, 'html.parser')
    info=Soup.find_all(class_="txt_green letter_space")
    count=0
    
    for items in info:
        count+=1
        if count==2:

            data=items.get_text()
    
    silver=float(data.replace('Rs.', ''))
    print(silver)
    gold_nisab=round((gold*7.5),2)
    silver_nisab= round((silver*52.5),2)
    b=date.today()
    if request.method=='POST':
        form=ZakatForm(request.POST)
        if form.is_valid():
            return HttpResponse("All good")
    else:
        form=ZakatForm()
    context={
        'age':a,
        'gold':gold,
        'silver':silver,
        'gold_nisab':gold_nisab,
        'silver_nisab':silver_nisab,
        'date': b,
        'form_k':form,

    }
    return render(request, 'index.html', context=context)

def gold(request):
    a=23
    b=date.today()
    context={
        'age':a,
        'date': b,

    }
    return render(request, 'gold.html', context=context)

def silver(request):
    a=23
    b=datetime.now()
    context={
        'age':a,
        'date': b,

    }
    return render(request, 'silver.html', context=context)

