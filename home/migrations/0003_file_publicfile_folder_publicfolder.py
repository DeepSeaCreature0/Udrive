# Generated by Django 4.2.2 on 2023-07-05 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_file_split_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='publicFile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='folder',
            name='publicFolder',
            field=models.BooleanField(default=False),
        ),
    ]