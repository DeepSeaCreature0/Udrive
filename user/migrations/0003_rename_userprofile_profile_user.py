# Generated by Django 4.2.2 on 2023-07-03 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_user_profile_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='userprofile',
            new_name='user',
        ),
    ]
