from django.contrib import admin
from .models import Sofa, Bed, Dining
# Register your models here.

class SofaAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price_base_unit', 'condition', 'material', 'softness')


class BedAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price_base_unit', 'condition', 'material', 'storage')


class DiningAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price_base_unit', 'condition', 'material')


admin.site.register(Sofa, SofaAdmin)
admin.site.register(Bed, BedAdmin)
admin.site.register(Dining, DiningAdmin)