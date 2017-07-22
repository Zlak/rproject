from django.shortcuts import render
from .models import Article, Term, ProjectInfo

def home_page(request):
    return render(request, 'main.html')


def articles(request):
    article = Article.objects.first()
    return render(request, 'articles.html', {'article': article})


def services(request):
    return render(request, 'services.html')

def thesaurus(request):
    terms = Term.objects.all
    return render(request, 'thesaurus.html', {'terms': terms})

def projectinfo(request):
    _info_ = ProjectInfo.objects.first()
    return render(request, 'projectinfo.html', {'projectinfo': _info_})

def prediction(request):

    return render(request, 'prediction.html',)
