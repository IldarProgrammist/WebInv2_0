# Generated by Django 3.1.1 on 2020-11-04 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('printer', '0006_auto_20201104_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catriege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialNumber', models.CharField(max_length=100, verbose_name='Серийный номер')),
                ('original', models.BooleanField(verbose_name='Оригинальный')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printer.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Картридж',
                'verbose_name_plural': 'Картриджи',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Цвет')),
                ('word', models.CharField(max_length=1, unique=True, verbose_name='Обозначение')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус картриджа',
                'verbose_name_plural': 'Статусы картриджей',
            },
        ),
        migrations.CreateModel(
            name='CatrigeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название модели картриджа')),
                ('fhoto', models.ImageField(blank=True, upload_to='', verbose_name='Фото')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catriges.color', verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Модель картриджа',
                'verbose_name_plural': 'Модели картриджей',
            },
        ),
        migrations.CreateModel(
            name='CatrigeJurnal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appeal', models.CharField(max_length=100, unique=True, verbose_name='Заявка')),
                ('date', models.DateField(verbose_name='Дата регистрации')),
                ('discription', models.TextField(blank=True, verbose_name='Описание')),
                ('serialNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catriges.catriege', verbose_name='Серийный номер')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catriges.status', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Журнал картриджа',
                'verbose_name_plural': 'Журналы картриджей',
            },
        ),
        migrations.AddField(
            model_name='catriege',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catriges.catrigemodel', verbose_name='Модель картриджа'),
        ),
    ]