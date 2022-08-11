from django.contrib import admin
from expenseapp.models import (Expense, Profile, Customer,
    ExpenseType, ExpenseData, ExpenseTypeField)

# Register your models here.
admin.site.register(Expense)
admin.site.register(ExpenseData)
admin.site.register(ExpenseType)
admin.site.register(ExpenseTypeField)
admin.site.register(Profile)
admin.site.register(Customer)
