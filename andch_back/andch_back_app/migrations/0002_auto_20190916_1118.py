# Generated by Django 2.2.5 on 2019-09-16 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('andch_back_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='imagePath',
            new_name='clientImagePath',
        ),
    ]