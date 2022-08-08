# Generated by Django 4.0.6 on 2022-07-29 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0049_remove_product_amount_remove_windowmodel_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedestalmodel',
            name='measurement2',
        ),
        migrations.AlterField(
            model_name='pedestalmodel',
            name='measurement',
            field=models.CharField(choices=[('PM', 'П.М'), ('SHT', 'ШТ'), ('PM and SHT', 'П.М и ШТ')], default='PM', max_length=10, verbose_name='единица измерения'),
        ),
    ]
