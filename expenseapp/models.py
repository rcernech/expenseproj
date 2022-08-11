from django.db import models

# Create your models here.
class Profile(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    status = models.CharField(max_length=100)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    customerNumber = models.IntegerField()
    status = models.CharField(max_length=100)

"""
class Expense_bak(models.Model):
    customerId = models.ForeignKey(Customer,related_name='customer',on_delete=models.CASCADE)
    employeeId = models.ForeignKey(Profile,related_name='employee',on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    billable = models.BooleanField()
"""

class Expense(models.Model):
    customerId = models.ForeignKey(Customer,related_name='customer',on_delete=models.CASCADE)
    employeeId = models.ForeignKey(Profile,related_name='employee',on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    billable = models.BooleanField()
    vendor = models.CharField(max_length=100, blank=True, null=True)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    origin = models.CharField(max_length=100, blank=True, null=True)
    destination = models.CharField(max_length=100, blank=True, null=True)
    miles = models.PositiveIntegerField(blank=True, null=True)
    attendees = models.CharField(max_length=250, blank=True, null=True)

class ExpenseData(models.Model):
    key = models.CharField(max_length=250)
    value = models.CharField(max_length=250)
    # expense = models.ForeignKey(Expense,related_name='expense_data',on_delete=models.CASCADE)

class ExpenseType(models.Model):
    name = models.CharField(max_length=100)

class ExpenseTypeField(models.Model):
    expenseType = models.ForeignKey(ExpenseType,related_name='expense_type_fields',on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
