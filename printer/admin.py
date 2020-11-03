from django import forms
from django.contrib import admin
from printer.models import *


@admin.register(PrinterModel)
class PrinterFirmAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(PrinterFirm)
class PrinterModelAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(PrinterStatus)
class PrinterStatusAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ['name','serialNumber','category','printerModel']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return PrinterChoiceField(Category.objects.filter(slug='printers'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class PrinterChoiceField(forms.ModelChoiceField):
    pass


@admin.register(JurnalPrinter)
class JurnalPrinterAdmin(admin.ModelAdmin):
    list_display = ['serialNumber','status', 'date']
