from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .random_number import *
from .models import *
from playsound import playsound

# Create your views here.

def index(request):
    return render(request, "callnumber/home.html")


def main_page(request):
    already_called = []
    num = None
 
    if request.method == "POST":
        # pick a number
        if request.POST.get("pick"):
            already_called = randomNum().copy()
            if len(already_called) > 89:
                already_called = reset().copy()
            num = already_called[-1]
            playsound('/Users/daivuong/loto/static/sound/%d.wav' %num)
            print(len(already_called))
        # reset the game        
        elif request.POST.get("reset"):
            already_called = reset().copy()
                
    over_msg = len(already_called)
    
    # generate the number table
    total = []
    for i in range(1,91):
        total.append(i)

    cut_line = [11, 21, 31, 41, 51, 61, 71, 81]
    context = {"picked":already_called, "num":num, "total":total, "cut_line":cut_line, "over_msg":over_msg}
    return render(request, "callnumber/mainPage.html", context)
