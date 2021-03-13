from django.contrib import admin
from testapp.models import FilterModel


class FilterModelAdmin(admin.ModelAdmin):
    list_dislay = ['name', 'subject', 'dept', 'date']

# Register your models here.


admin.site.register(FilterModel, FilterModelAdmin)