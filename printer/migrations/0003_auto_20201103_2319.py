# Generated by Django 3.1.1 on 2020-11-03 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printer', '0002_printer_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurnalprinter',
            name='discription',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jurnalprinter',
            name='serialNumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printer.printer', verbose_name='Имя принтера'),
        ),
    ]