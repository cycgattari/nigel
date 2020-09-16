from django.contrib import admin
from .models import Page, Unidades, Mediciones
# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title','update_date', 'permalink')
    ordening = ('title',)
    search_fields = ('title',)


admin.site.register(Page, PageAdmin)
admin.site.register(Unidades)
admin.site.register(Mediciones)
