# Generated by Django 3.1.5 on 2021-05-17 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='precent',
            new_name='percent',
        ),
    ]
