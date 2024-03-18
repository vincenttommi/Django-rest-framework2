from django.urls  import path
from core import  views 
from core import views
from rest_framework import routers


router  = routers.SimpleRouter()
#routing allows to quickly declare  all of  common routes for given resource controller


router.register(r'categories', views.CategoryModelViewSet,  basename="category")
router.register(r'transactions', views.TransactionModelViewSet, basename="transaction")
#using routers  for ViewSets

urlpatterns = [
    path("currencies/", views.CurrencyListAPIView.as_view() ,  name="currencies")
] + router.urls
