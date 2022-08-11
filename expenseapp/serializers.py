from django.contrib.auth.models import User, Group
from expenseapp.models import Expense, Profile, Customer, ExpenseData
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ExpenseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseData
        fields = ['key', 'value']

class ExpenseSerializer(serializers.ModelSerializer):
    # expense_data = ExpenseDataSerializer(many=True, read_only=False)

    class Meta:
        model = Expense
        # fields = ['id', 'customerId', 'employeeId', 'description', 'type', 'status', 'amount', 'billable', 'expense_data']
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
