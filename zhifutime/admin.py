from django.contrib import admin
from .models import Contact, Service, Term


class ContactAdmin(admin.ModelAdmin):
    list_display = ('text',)


class TermAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
    search_fields = ('title', 'text')
    ordering = ['title']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'price')
    ordering = ('title', 'price')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Term, TermAdmin)
admin.site.register(Service, ServiceAdmin)
