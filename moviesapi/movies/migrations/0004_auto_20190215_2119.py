# Generated by Django 2.1.7 on 2019-02-15 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20190215_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='actor',
            new_name='movie_cast_in',
        ),
    ]
