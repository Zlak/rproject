from django.shortcuts import render, get_object_or_404
from .models import Article, Term, ProjectInfo, MainPageInfo


def home_page(request):
    return render(request, 'main.html')


def articles(request):
    articles_ = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles_})


def article_id(request, art_id):
    article = get_object_or_404(Article, id=art_id)
    return render(request, 'article.html', {'article': article})


def services(request):
    return render(request, 'services.html')


def thesaurus(request):
    terms = Term.objects.all
    return render(request, 'thesaurus.html', {'terms': terms})


def projectinfo(request):
    _info_ = ProjectInfo.objects.first()
    return render(request, 'projectinfo.html', {'projectinfo': _info_, 'pagetitle': 'О проекте'})


# def mainpageinfo(request):
#     _info_ = MainPageInfo.objects.first()
#     return render(request, 'projectinfo.html', {'projectinfo': _info_, 'pagetitle': 'Китайская метафизика'})
def mainpageinfo(request):
    article = Article.objects.first()
    return render(request, 'main.html', {'article': article})


def prediction(request):
    return render(request, 'prediction.html',)
