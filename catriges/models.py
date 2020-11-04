from printer.models import *
class Color(models.Model):
    name = models.CharField(max_length=30, verbose_name='Цвет', unique=True)
    word = models.CharField(max_length=1, verbose_name='Обозначение', unique=True)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name


class CatrigeModel(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название модели картриджа', unique=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Цвет')
    fhoto = models.ImageField(verbose_name='Фото', blank=True)

    class Meta:
        verbose_name = 'Модель картриджа'
        verbose_name_plural = 'Модели картриджей'


    def __str__(self):
        return self.name



class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус', unique=True)


    class Meta:
        verbose_name = 'Статус картриджа'
        verbose_name_plural = 'Статусы картриджей'

    def __str__(self):
        return self.name


class Catriege(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    serialNumber = models.CharField(max_length=100, verbose_name='Серийный номер')
    model = models.ForeignKey(CatrigeModel, models.CASCADE, verbose_name='Модель картриджа')
    original = models.BooleanField(verbose_name='Оригинальный')

    class Meta:
        verbose_name = 'Картридж'
        verbose_name_plural = 'Картриджи'

    def __str__(self):
        return self.serialNumber

    def get_absolute_url(self):
        return reverse('catrigeList')



class CatrigeJurnal(models.Model):
    appeal = models.CharField(max_length=100, verbose_name='Заявка', unique=True)
    serialNumber = models.ForeignKey(Catriege, on_delete=models.CASCADE, verbose_name='Серийный номер')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    date = models.DateField(verbose_name='Дата регистрации')
    discription = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.appeal

    def get_absolute_url(self):
        return reverse('jurnal_catrige_list')

    class Meta:
        verbose_name = 'Журнал картриджа'
        verbose_name_plural = 'Журналы картриджей'

