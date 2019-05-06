from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Article, Term, ProjectInfo, MainPageInfo
from hitcount.views import HitCountDetailView

def home_page(request):
    return render(request, 'main.html')


def articles(request):
    articles_ = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles_})



class ArticleId(HitCountDetailView, TemplateView):

    template_name = 'article.html'
    model = Article
    count_hit = True

    def get_context_data(self, **kwargs):
        art_id = self.kwargs['art_id']
        self.object = get_object_or_404(Article, id=art_id)
        #context = super(HitCountDetailView, self).get_context_data(**kwargs)
        context = super(ArticleId, self).get_context_data(**kwargs)
        #context['article'] = article

        return context

    #request, art_id):
    #article = get_object_or_404(Article, id=art_id)
    #return render(request, 'article.html', {'article': article})


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
