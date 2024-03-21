# core/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Currency, Category, Transaction

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("id","code","name")

class CategorySerializer(serializers.ModelSerializer):
    user  = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Category
        fields = ("id","name", "user")


class WriteTransactionSerializer(serializers.ModelSerializer):
    user  = serializers.HiddenField(default=serializers.CurrentUserDefault())
    currency = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())
    class Meta:
        model = Transaction
        fields = ("user","amount","currency","date","description","category")
        
        
        
    def  __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset
        user  = self.context["request"].user
        self.fields["category"].queryset  = user.categories.all()
        
        
class ReadUserSerializer(serializers.ModelSerializer):
    class Meta: 
        model  = User 
        fields  = ("id","username", "first_name","last_name")
        read_only_fields = fields
        
        
        
        
        
class ReadTransactionSerializer(serializers.ModelSerializer):
    user = ReadUserSerializer()
    currency = CurrencySerializer()
    category  =  CategorySerializer()
    

    class Meta:
        model = Transaction
        fields = ("id","amount","currency","description","category","user")
        read_only_fields  = ['amount','currency','date','description','catgeory']
