# Generated by Django 2.1.7 on 2019-02-15 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20190215_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='age',
            field=models.IntegerField(),
        ),
    ]
