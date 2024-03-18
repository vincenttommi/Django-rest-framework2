from rest_framework import serializers 
from .models import Currency,Category,Transaction






class  CurrencySerializer(serializers.ModelSerializer):
    class  Meta:
        model =  Currency
        fields = '__all__'     #serializes all fields of the  Currency model in the serializer
        
        
        
        
class CategorySerializer(serializers.ModelSerializer):
      class Meta:
          model  = Category
          fields = '__all__'  # serializes all fields of the Category model in the serializer        
 
 
 
 
 
class  WriteTransactionSerializer(serializers.ModelSerializer):
    
    
    currency = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())
    #recording transaction with field names instead of codes
    
    class Meta:
        model = Transaction
        fields = '__all__'       
        
        
class ReadTransactionSerializer(serializers.ModelSerializer):
            
        currency = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())
        
        class Meta:
            model  = Transaction
            fields = '__all__'   