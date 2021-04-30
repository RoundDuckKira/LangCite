# Generated by Django 3.1.4 on 2021-04-24 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('langImport', '0017_auto_20210424_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fdictionary',
            name='lang_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr_lang1', to='langImport.englishword'),
        ),
        migrations.AlterField(
            model_name='fdictionary',
            name='lang_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr_lang2', to='langImport.spanishword'),
        ),
        migrations.AlterField(
            model_name='fdictionary',
            name='lang_3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr_lang3', to='langImport.russianword'),
        ),
        migrations.AlterField(
            model_name='rdictionary',
            name='lang_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ru_lang1', to='langImport.englishword'),
        ),
        migrations.AlterField(
            model_name='rdictionary',
            name='lang_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ru_lang2', to='langImport.spanishword'),
        ),
        migrations.AlterField(
            model_name='rdictionary',
            name='lang_3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ru_lang3', to='langImport.frenchword'),
        ),
        migrations.AlterField(
            model_name='sdictionary',
            name='lang_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spa_lang1', to='langImport.englishword'),
        ),
        migrations.AlterField(
            model_name='sdictionary',
            name='lang_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spa_lang2', to='langImport.russianword'),
        ),
        migrations.AlterField(
            model_name='sdictionary',
            name='lang_3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spa_lang3', to='langImport.frenchword'),
        ),
    ]
