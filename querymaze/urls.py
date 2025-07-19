from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, TopCustomerApiView, OrderReportApiView, BestSellingProduct

# router = DefaultRouter()
# router.register('customer',CustomerViewSet)
# router.register('order',OrderViewSet)
urlpatterns = [
path('customer/',CustomerViewSet.as_view(),name='customer'),
path('top-customers/',TopCustomerApiView.as_view(),name='top-customer'),
path('order-report/',OrderReportApiView.as_view(),name='order-report'),
path('best-selling-product/',BestSellingProduct.as_view(),name='best-selling-product'),
]