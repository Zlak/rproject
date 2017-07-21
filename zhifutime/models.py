from django.db import models


class Contact(models.Model):
    text = models.CharField(max_length=200)


class Term(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField()

class Service(models.Model):
    title = models.CharField(default='', max_length=80)
    desc = models.TextField()
    price = models.CharField(max_length=80)
