from django.views.generic import TemplateView



class IndexView(TemplateView):
    template_name = 'mainapp/index.html'




class PrinterInfo(TemplateView):
    template_name = 'printer/printer_info.html'