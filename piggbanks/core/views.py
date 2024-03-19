# from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Currency, Category, Transaction
from rest_framework.pagination import PageNumberPagination  
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import CategorySerializer, CurrencySerializer, ReadTransactionSerializer, WriteTransactionSerializer

class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = None

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination

class TransactionModelViewSet(ModelViewSet):
    queryset = Transaction.objects.select_related("currency", "category")
    filter_backends = [SearchFilter, OrderingFilter,]
    search_fields = ["description"]
    ordering_fields = ("amount", "date")  # Corrected typo here
    # filterset_fields = ("currency__code")
    
    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadTransactionSerializer
        return WriteTransactionSerializer
