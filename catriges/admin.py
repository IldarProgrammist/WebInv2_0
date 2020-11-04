from django import forms
from django.contrib import admin
from catriges.models import Color, CatrigeModel, Status, Catriege, CatrigeJurnal, Category


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name',  'word']


@admin.register(CatrigeModel)
class CatrigeModelAdmin(admin.ModelAdmin):
    list_display = ['name','color']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']


class CatrigeChoiceField(forms.ModelChoiceField):
    pass

@admin.register(Catriege)
class CatriegeAdmin(admin.ModelAdmin):
    list_display = ['category','serialNumber','model','original']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return CatrigeChoiceField(Category.objects.filter(slug='catriges'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)









@admin.register(CatrigeJurnal)
class CatrigeJurnalAdmin(admin.ModelAdmin):
    list_display = ['appeal','serialNumber','status','date']





