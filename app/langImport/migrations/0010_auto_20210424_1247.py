# Generated by Django 3.1.4 on 2021-04-24 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('langImport', '0009_auto_20210424_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='englishword',
            name='definition',
            field=models.TextField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='englishword',
            name='pron',
            field=models.CharField(default='none2', max_length=20),
        ),
        migrations.AddField(
            model_name='englishword',
            name='word',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='englishword',
            name='word_class',
            field=models.CharField(default='none', max_length=20),
        ),
    ]
