# Generated by Django 4.1 on 2022-08-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenseapp', '0006_remove_expensetype_expensefields_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='employeeId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
