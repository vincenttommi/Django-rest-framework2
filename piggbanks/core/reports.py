from dataclasses import dataclass
from decimal import Decimal
from  core.models  import Category, Transaction
from django.db.models  import Sum, Count, Avg






@dataclass 
class ReportEntry:
    category:Category
    total : Decimal
    count : int
    avg : Decimal

def transaction_report():
    
    data  = []
    
    queryset =  Transaction.objects.values("category").annotate(
        total=Sum("amount"),
        count=Count("id"),
        avg=Avg("amount"),
    )
    return  queryset 


    categories_index  = {}
    for category in Category.objects.all():
        categories_index[Category.pk] = category

        for entry  in queryset:
        
         category =  Category.objects.get(pk=entry["category"])
        #getting category instance from database
        report_entry  = ReportEntry(category , entry["total"], entry["count"], entry["avg"]) 
        data.append(report_entry) 
        
        return queryset
    