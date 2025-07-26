from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..views.views import CustomerViewSet, TopCustomerApiView, OrderReportApiView, BestSellingProduct
from ..views.createOrderView import OrderCreateApiView
from ..views.topCustomerView import TopCustomerApiView
from ..views.orderByCustomerView import OrderByCustomerApiView
from ..views.salesByDay import SalesByDay
from ..views.customerNoOrderView import CustomerNoOrdersView
from ..views.unsoldProductsView import UnsoldProductView
from ..views.monthlySalesView import MonthlySales
from ..views.topCustomerByCityView import TopCustomerByCity
from ..views.topLocationView import TopLocationApiView

router = DefaultRouter()
router.register(r'customer',OrderByCustomerApiView,basename='customer'),
urlpatterns = [
path('customer/',CustomerViewSet.as_view(),name='customer'),
path('top-customers/',TopCustomerApiView.as_view(),name='top-customer'),
path('order-report/',OrderReportApiView.as_view(),name='order-report'),
path('best-selling-product/',BestSellingProduct.as_view(),name='best-selling-product'),
path('order/create/',OrderCreateApiView.as_view(),name='order-create'),
path('top-customer/',TopCustomerApiView.as_view(),name='top-customer'),
path('sales-by-day/',SalesByDay.as_view(),name='sales-by-day'),
path('customer-no-order/',CustomerNoOrdersView.as_view(),name='customer-no-order'),
path('unslod-product/',UnsoldProductView.as_view(),name='unslod-product'),
path('monthly-sales/',MonthlySales.as_view(),name='monthly-sales'),
path('top-customer-by-city/',TopCustomerByCity.as_view(),name='top-customer-by-city'),
path('top-location/',TopLocationApiView.as_view(),name='top-location'),  
path('', include(router.urls)),
path('',include('querymaze.urls.customerUrls'))
]