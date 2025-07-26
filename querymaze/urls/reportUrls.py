from django.urls import path
from ..views.reports.topCustomerViews import TopCustomerApiView
from ..views.reports.salesByDayViews import SalesByDayApiView
from ..views.reports.monthlySalesViews import MonthlySalesApiView
from ..views.reports.topCustomerByCityViews import TopCustomerByCity
from ..views.reports.topLocationViews import TopLocationApiView
from ..views.reports.customerNoOrderView import CustomerNoOrdersApiView
from ..views.reports.orderReportViews import OrderReportApiView

urlpatterns= [
    path('top-customers/',TopCustomerApiView.as_view(),name='top-customers'),
    path('sales-by-day/',SalesByDayApiView.as_view(),name='sales-by-day'),
    path('monthly-sales/',MonthlySalesApiView.as_view(),name='monthly-sales'),
    path('top-customer-by-city/',TopCustomerByCity.as_view(),name='top-customer-by-city'),
    path('top-location/',TopLocationApiView.as_view(),name='top-location'),
    path('customer-no-order/',CustomerNoOrdersApiView.as_view(),name='customer-no-order'),
    path('order-report/',OrderReportApiView.as_view(),name='order-report'),  
]