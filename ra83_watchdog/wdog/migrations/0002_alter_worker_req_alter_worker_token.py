# Generated by Django 4.0.5 on 2022-06-22 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wdog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='req',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='worker',
            name='token',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
