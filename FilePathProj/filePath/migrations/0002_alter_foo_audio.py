# Generated by Django 4.1.4 on 2022-12-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filePath', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foo',
            name='audio',
            field=models.FilePathField(match='*.mp4', max_length=150, path='E:\\PIPING.STRESS', recursive=True),
        ),
    ]
