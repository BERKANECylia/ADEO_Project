from django.shortcuts import render


def home(request):
    return render(request, 'homescreen/home.html')



def about(request):
    return render(request, 'homescreen/about.html')