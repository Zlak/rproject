from django.db import models
from tinymce import models as tinymce_models


class Contact(models.Model):
    text = models.CharField(max_length=200)


class Term(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField()

    class Meta:
        ordering = ['title']


class Service(models.Model):
    title = models.CharField(default='', max_length=80)
    desc = models.TextField()
    price = models.CharField(max_length=80)


class Article(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, default='', null=True, blank=True,
                            help_text='Краткое описание статьи')
    text = tinymce_models.HTMLField()


class ProjectInfo(models.Model):
    text = tinymce_models.HTMLField()
