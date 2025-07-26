from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..views.views import CustomerViewSet, OrderReportApiView, BestSellingProduct
from ..views.createOrderView import OrderCreateApiView
from ..views.orderByCustomerView import OrderByCustomerApiView
from ..views.unsoldProductsView import UnsoldProductView


router = DefaultRouter()
router.register(r'customer',OrderByCustomerApiView,basename='customer'),
urlpatterns = [
path('customer/',CustomerViewSet.as_view(),name='customer'),
path('order-report/',OrderReportApiView.as_view(),name='order-report'),
path('best-selling-product/',BestSellingProduct.as_view(),name='best-selling-product'),
path('order/create/',OrderCreateApiView.as_view(),name='order-create'),
path('unslod-product/',UnsoldProductView.as_view(),name='unslod-product'),
path('', include(router.urls)),
path('',include('querymaze.urls.customerUrls')),
path('',include('querymaze.urls.reportUrls'))
]