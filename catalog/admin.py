from django.contrib import admin

from .models import Beer, Producer, Style, Category


@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    list_display = ('name', 'volume', 'producer', 'score')


class ProducerAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'brewer')


admin.site.register(Producer, ProducerAdmin)
admin.site.register(Style)
admin.site.register(Category)
