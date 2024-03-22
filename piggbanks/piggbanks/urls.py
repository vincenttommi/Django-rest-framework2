from django.urls  import path
from core import  views 
from core import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
# importing authentification token from  rest framework
router  = routers.SimpleRouter()
#routing allows to quickly declare  all of  common routes for given resource controller


router.register(r'categories', views.CategoryModelViewSet,  basename="category")
router.register(r'transactions', views.TransactionModelViewSet, basename="transaction")
#using routers  for ViewSets

urlpatterns = [
    path("login/", obtain_auth_token, name="obtain-auth-token"),
    path("currencies/", views.CurrencyListAPIView.as_view() ,  name="currencies"),
    path("report/", views.TransactionReportAPIView.as_view(), name="report"),
] + router.urls
