# core/serializers.py

from rest_framework import serializers
from .models import Currency, Category, Transaction

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class WriteTransactionSerializer(serializers.ModelSerializer):
    currency = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())
    class Meta:
        model = Transaction
        fields = '__all__'

class ReadTransactionSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields  = ['amount','currency','description','date','category']
