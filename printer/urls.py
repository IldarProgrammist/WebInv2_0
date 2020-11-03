from django.urls import path
from printer.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',PrinterInfoView.as_view(),name='print'),
    path('list/', PrinterListView.as_view(), name='printerList'),
    path('detile/<int:pk>/', login_required(PrinterDetileView.as_view()), name='printer_detail'),
    path('jurnal/list', login_required(JurnalPrinterListView.as_view()), name='jurnal_printer'),
    path('jurnal/create/', login_required(JurnalPrinterCreate.as_view()), name='create_jurnal_printer'),

]