# Generated by Django 4.2 on 2023-04-30 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Donor',
        ),
        migrations.DeleteModel(
            name='Orphanage',
        ),
    ]