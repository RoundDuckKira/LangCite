# Generated by Django 3.1.4 on 2021-04-01 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('langImport', '0002_auto_20210401_1556'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
    ]