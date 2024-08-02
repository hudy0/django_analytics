from django.db.models import QuerySet
from rest_framework import viewsets

from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Customer] = Customer.objects.all()
    serializer_class = CustomerSerializer
