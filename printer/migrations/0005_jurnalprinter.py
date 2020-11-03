# Generated by Django 3.1.1 on 2020-11-03 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printer', '0004_printer'),
    ]

    operations = [
        migrations.CreateModel(
            name='JurnalPrinter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apper', models.CharField(max_length=100, unique=True, verbose_name='Обращение')),
                ('date', models.DateField(verbose_name='Дата')),
                ('serialNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printer.printer', verbose_name='Серийный номер принтера')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printer.printerstatus', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Журнал принтера',
                'verbose_name_plural': 'Журналы принтеров',
            },
        ),
    ]
