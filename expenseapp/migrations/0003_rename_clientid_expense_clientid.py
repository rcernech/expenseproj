# Generated by Django 4.1 on 2022-08-09 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenseapp', '0002_rename_user_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='clientid',
            new_name='clientId',
        ),
    ]