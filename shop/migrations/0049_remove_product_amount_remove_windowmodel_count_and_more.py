# Generated by Django 4.0.6 on 2022-07-29 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0048_remove_pedestalmodel_count_pedestalmodel_choice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='windowmodel',
            name='count',
        ),
        migrations.AddField(
            model_name='pedestalmodel',
            name='measurement2',
            field=models.CharField(choices=[('PM', 'П.М'), ('SHT', 'ШТ')], default='PM', max_length=10, verbose_name='единица измерения'),
        ),
    ]
