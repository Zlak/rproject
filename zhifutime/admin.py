from django.contrib import admin
from .models import Contact, Service, Term, Article, ProjectInfo, MainPageInfo


class ContactAdmin(admin.ModelAdmin):
    list_display = ('text',)


class TermAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
    search_fields = ('title', 'text')
    ordering = ['title']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'price')
    ordering = ('title', 'price')


class ProjectinfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'desc', 'publish')
    search_fields = ('title', 'text')
    ordering = ('-publish', 'title')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Term, TermAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ProjectInfo, ProjectinfoAdmin)
admin.site.register(MainPageInfo, ProjectinfoAdmin)