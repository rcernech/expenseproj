# Generated by Django 4.1 on 2022-08-10 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenseapp', '0005_remove_expense_expensedata_expensedata_expense'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expensetype',
            name='expenseFields',
        ),
        migrations.AddField(
            model_name='expensetypefield',
            name='expenseType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='expense_type_fields', to='expenseapp.expensetype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expensedata',
            name='expense',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expense_data', to='expenseapp.expense'),
        ),
    ]
