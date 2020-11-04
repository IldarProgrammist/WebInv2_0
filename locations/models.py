from django.db import models

class Titul(models.Model):
    number = models.CharField(max_length=100, verbose_name='Номер титула', unique=True)
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Титул'
        verbose_name_plural = 'Титулы'


class Room(models.Model):
    titul = models.ForeignKey(Titul,on_delete=models.CASCADE, verbose_name='Титул')
    number = models.CharField(max_length=100, verbose_name='Номер кабинета')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'
