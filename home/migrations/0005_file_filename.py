# Generated by Django 4.2.2 on 2023-07-06 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_file_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='filename',
            field=models.CharField(default='', max_length=200),
        ),
    ]
