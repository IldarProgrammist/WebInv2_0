from django.db import models
from django.urls import reverse

from locations.models import Room


class PrinterModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название модели')
    img = models.ImageField(verbose_name='Фото', blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель принтера'
        verbose_name_plural = 'Модель принтеров'

class PrinterFirm(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название фирмы', unique=True)
    printerModel = models.ManyToManyField(PrinterModel, verbose_name='Модель принтера')
    img = models.ImageField(verbose_name='Логотип', blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фирма принтера'
        verbose_name_plural = 'Фирмы принтеров'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория', unique= True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class PrinterStatus(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус')
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус принтера'
        verbose_name_plural = 'Статусы принтеров'



class Printer(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=40, verbose_name='Имя принтера', unique=True)
    ip_adress = models.CharField(max_length=50, verbose_name='Ip-адрес', unique=True)
    serialNumber = models.CharField(max_length=100, verbose_name='Серийный номер', unique=True)
    printerModel = models.ForeignKey(PrinterModel, on_delete=models.Case, verbose_name='Модель принтера')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтеры'



class JurnalPrinter(models.Model):
    apper = models.CharField(max_length=100, verbose_name='Обращение', unique=True)
    serialNumber = models.ForeignKey(Printer, on_delete=models.CASCADE, verbose_name='Имя принтера')
    status = models.ForeignKey(PrinterStatus,on_delete=models.CASCADE, verbose_name='Статус')
    location = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Кабинет')
    date = models.DateField(verbose_name='Дата')
    discription = models.TextField(verbose_name='Описание', blank=True)
    def __str__(self):
        return self.apper

    class Meta:
        verbose_name = 'Журнал принтера'
        verbose_name_plural = 'Журналы принтеров'

    def get_absolute_url(self):
        return reverse('jurnal_printer')



