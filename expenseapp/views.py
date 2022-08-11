from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, generics
from expenseapp.models import Expense, Profile, Customer
from expenseapp.serializers import UserSerializer, GroupSerializer
from expenseapp.serializers import ExpenseSerializer, ProfileSerializer, CustomerSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filterset_fields = ['customerId', 'employeeId', 'startDate']
    permission_classes = [permissions.IsAuthenticated]

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filterset_fields = ['customerId', 'employeeId', 'startDate']
    permission_classes = [permissions.IsAuthenticated]

class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_fields = ['customerId', 'employeeId', 'startDate']
    permission_classes = [permissions.IsAuthenticated]
