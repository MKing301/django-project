# Generated by Django 3.1.7 on 2021-05-14 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210510_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]