from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

from tinymce import models as tinymce_models
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin

class Contact(models.Model):
    text = models.CharField(max_length=200)


class Term(models.Model):
    title = models.CharField(max_length=80)
    text = tinymce_models.HTMLField()

    class Meta:
        ordering = ['title']
        verbose_name = 'Термин'
        verbose_name_plural = 'Термины'


class Service(models.Model):
    title = models.CharField(default='', max_length=80)
    desc = models.TextField()
    price = models.CharField(max_length=80)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Article(models.Model, HitCountMixin):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    desc = models.CharField(max_length=350, default='', null=True, blank=True,
                            help_text='Краткое описание статьи')
    text = tinymce_models.HTMLField()
    publish = models.DateTimeField(default=timezone.now)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def get_absolute_url(self):
        return reverse('article_id', args=[self.id])


class ProjectInfo(models.Model):
    text = tinymce_models.HTMLField()


class MainPageInfo(models.Model):
    text = tinymce_models.HTMLField()