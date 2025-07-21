from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.views import CustomerViewSet, TopCustomerApiView, OrderReportApiView, BestSellingProduct
from .views.createOrderView import OrderCreateApiView
from .views.topCustomerView import TopCustomerApiView
from .views.orderByCustomerView import OrderByCustomerApiView
from .views.salesByDay import SalesByDay

router = DefaultRouter()
router.register(r'customer',OrderByCustomerApiView)

urlpatterns = [
path('customer/',CustomerViewSet.as_view(),name='customer'),
path('top-customers/',TopCustomerApiView.as_view(),name='top-customer'),
path('order-report/',OrderReportApiView.as_view(),name='order-report'),
path('best-selling-product/',BestSellingProduct.as_view(),name='best-selling-product'),
path('order/create/',OrderCreateApiView.as_view(),name='order-create'),
path('top-customer/',TopCustomerApiView.as_view(),name='top-customer'),
path('sales-by-day/',SalesByDay.as_view(),name='sales-by-day'),
path('', include(router.urls)),
]

