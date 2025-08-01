from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..views.customerViews import CustomerApiView, DeleteCustomerApiView, DuplicatesCustomerApiView

router = DefaultRouter()
router.register(r'customer',CustomerApiView,basename='customer')
router.register(r'customer',DeleteCustomerApiView,basename='delete-customer')

urlpatterns= [
path('duplicates-customer/',DuplicatesCustomerApiView.as_view(),name='duplicates-customer'),  
path('',include(router.urls))
]
