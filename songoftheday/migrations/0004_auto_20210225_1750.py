# Generated by Django 3.1.6 on 2021-02-25 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songoftheday', '0003_auto_20210225_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songmodel',
            old_name='interpreter',
            new_name='links',
        ),
    ]
