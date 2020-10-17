from django.contrib import admin

# Register your models here.
from .models import Commune, Deputy, District, Region


class DeputyAdmin(admin.ModelAdmin):
    list_display = ['name', 'district', 'politic_party']
    search_fields = ['name']

class CommuneAdmin(admin.ModelAdmin):
    list_display = ['name', 'district', 'region']
    search_fields = ['name']

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Deputy, DeputyAdmin)
admin.site.register(Commune, CommuneAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Region, RegionAdmin)
