from django.shortcuts import render


def home_page(request):
    return render(request, 'main.html')


def articles(request):
    return render(request, 'articles.html')


def services(request):
    return render(request, 'services.html')

def thesaurus(request):
    return render(request, 'thesaurus.html')

def projectinfo(request):
    return render(request, 'projectinfo.html')

def prediction(request):
    return render(request, 'prediction.html')
