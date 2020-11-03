from django.db.models import Q
from django.views.generic import *

from printer.forms import PrinterJurnalCreateForm
from printer.models import Printer, JurnalPrinter


class PrinterInfoView(TemplateView):
    template_name = 'printer/printer_info.html'



class PrinterListView(ListView):
    model = Printer
    template_name = 'printer/printerList.html'
    context_object_name = 'printer_'


    def get_queryset(self):
        query = self.request.GET.get('q',"")
        object_list =Printer.objects.filter(Q(serialNumber__contains=query)
                                            )
        return object_list


class JurnalPrinterListView(ListView):
    model = JurnalPrinter
    queryset = JurnalPrinter.objects.all()
    template_name = 'printer/jurnalListPrinter.html'
    paginate_by = 4
    context_object_name = 'jpl'


    def get_queryset(self):
        query = self.request.GET.get('q','')
        object_list =JurnalPrinter.objects.filter(
                                            Q(status__name =query)|
                                            Q(serialNumber__serialNumber__contains=query)
                                            )
        return object_list.order_by('-date')


class JurnalPrinterCreate(CreateView):
    model = JurnalPrinter
    form_class =  PrinterJurnalCreateForm
    template_name = 'printer/jurnalPrinterCreate.html'
    context_object_name = 'jplc'


class PrinterDetileView(DetailView):
    model = JurnalPrinter
    queryset = JurnalPrinter.objects.all()
    template_name = 'printer/printerDetile.html'
    context_object_name = 'printer'




