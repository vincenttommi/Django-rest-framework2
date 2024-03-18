from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from  .models import Currency,Category,Transaction
from .serializers import CategorySerializer,CurrencySerializer,TransactionSerializer



class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class  = CurrencySerializer
    
"""
In summary, this code defines a view (CurrencyListAPIView) that handles GET requests to retrieve a list of Currency objects. It fetches all Currency objects from the database and uses the CurrencySerializer to serialize them into JSON format for the HTTP response
"""
    

    
    
    
    #uses class based view approach
class CategoryModelViewSet(ModelViewSet):
    queryset  = Category.objects.all()
    serializer_class = CategorySerializer
    
    
 
 
 
 
class TransactionModelViewSet(ModelViewSet):
    queryset  = Transaction.objects.all()
    serializer_class = TransactionSerializer
     
     
     
    def get_serializer_class(self):
        return TransactionSerializer
    
    
        
    
    