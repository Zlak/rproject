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
    model = Article
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'desc', 'publish', 'get_hits')
    search_fields = ('title', 'text')
    ordering = ('-publish', 'title', 'hit_count_generic__hits')

    def get_hits(self, obj):
        return obj.hit_count.hits
    get_hits.admin_order_field = 'hit_count_generic__hits'  #Allows column order sorting
    get_hits.short_description = 'Hits'  #Renames column head

admin.site.register(Contact, ContactAdmin)
admin.site.register(Term, TermAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ProjectInfo, ProjectinfoAdmin)
admin.site.register(MainPageInfo, ProjectinfoAdmin)