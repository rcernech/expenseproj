# Generated by Django 4.1 on 2022-08-10 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenseapp', '0003_rename_clientid_expense_clientid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseTypeField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='description',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('expenseFields', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expense_fields', to='expenseapp.expensetypefield')),
            ],
        ),
    ]
