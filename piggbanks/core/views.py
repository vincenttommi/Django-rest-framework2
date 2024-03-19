# core/views.py

from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Currency, Category, Transaction
from .serializers import CategorySerializer, CurrencySerializer, ReadTransactionSerializer,  WriteTransactionSerializer

class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TransactionModelViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    
    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadTransactionSerializer
        return WriteTransactionSerializer
