# from rest_framework.filters import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Currency, Category, Transaction
from rest_framework.pagination import PageNumberPagination  
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import CategorySerializer, CurrencySerializer, ReadTransactionSerializer, WriteTransactionSerializer
from  rest_framework.permissions import IsAuthenticated

class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = None

class CategoryModelViewSet(ModelViewSet):
    permission_classes  = (IsAuthenticated,)
    #restricting for  only authenticated users to acess the views   
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # pagination_class = PageNumberPagination
    
    def  get_queryset(self):
        return Category.objects.filter(user=self.request.user)

class TransactionModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    #determines wether a  request should be granted or denied access
    #and are always run at ver start of the view
    filter_backends = [SearchFilter, OrderingFilter,]
    search_fields = ["description"]
    ordering_fields = ("amount", "date")  # Corrected typo here
    # filterset_fields = ("currency__code")
    
    def  get_queryset(self):
        return Transaction.objects.select_related("currency", "category", "user").filter(user=self.request.user)
        
    
    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadTransactionSerializer
        return WriteTransactionSerializer


    def perform_create(self, serializer):
         serializer.save(user=self.request.user)