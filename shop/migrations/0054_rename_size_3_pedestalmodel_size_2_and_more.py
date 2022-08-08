# Generated by Django 4.0.6 on 2022-07-29 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0053_remove_pedestalmodel_price_4'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedestalmodel',
            old_name='size_3',
            new_name='size_2',
        ),
        migrations.RemoveField(
            model_name='pedestalmodel',
            name='price_1',
        ),
        migrations.RemoveField(
            model_name='pedestalmodel',
            name='price_3',
        ),
        migrations.AddField(
            model_name='pedestalmodel',
            name='price_pm',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100, verbose_name='цена за ШТ'),
        ),
        migrations.AddField(
            model_name='pedestalmodel',
            name='price_sht',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100, verbose_name='цена за П.М'),
        ),
        migrations.AlterField(
            model_name='pedestalmodel',
            name='choice',
            field=models.CharField(choices=[('angular', 'наименование угловой'), ('facial', 'наименование лицовой'), ('name', 'наименование')], default='angular', max_length=10, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='pedestalmodel',
            name='choice_1',
            field=models.CharField(choices=[('top', 'Верхний часть'), ('average', 'Средний часть'), ('lower', 'Нижный часть'), ('top and lower', 'Верхний и нижный часть')], default='top', max_length=20, verbose_name='часть'),
        ),
        migrations.AlterField(
            model_name='pedestalmodel',
            name='measurement',
            field=models.CharField(choices=[('PM', 'П.М'), ('SHT', 'ШТ')], default='PM', max_length=10, verbose_name='единица измерения'),
        ),
        migrations.AlterField(
            model_name='pedestalmodel',
            name='price_2',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100, null=True, verbose_name='цена за ШТ или П.М'),
        ),
    ]
