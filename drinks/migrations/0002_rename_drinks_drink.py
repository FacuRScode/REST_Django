# Generated by Django 4.1.3 on 2022-11-05 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Drinks',
            new_name='Drink',
        ),
    ]