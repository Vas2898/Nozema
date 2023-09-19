from django.shortcuts import render



def home(request):
    return render(request,'shop/index.html')

def new(request):
    return render(request,'shop/register.html')    

    

