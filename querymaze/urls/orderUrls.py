from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..views.orderViews import OrderCreateApiView, OrderByCustomerApiView

router = DefaultRouter()
router.register(r'customer',OrderByCustomerApiView,basename='customer-orders'),

urlpatterns= [
    path('order/create/',OrderCreateApiView.as_view(),name='order-create'),
    path('',include(router.urls))
]