# Generated by Django 4.1.4 on 2023-01-05 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filePath', '0002_alter_foo_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foo',
            name='audio',
            field=models.FilePathField(match='*.mp4', path='E:\\PIPING.STRESS', recursive=True),
        ),
    ]
