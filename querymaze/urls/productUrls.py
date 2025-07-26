from django.urls import path
from ..views.productViews import UnsoldProductApiView, BestSellingProductApiView

urlpatterns= [
    path('unsold-product/',UnsoldProductApiView.as_view(),name='unsold-product'),
    path('best-selling-product/',BestSellingProductApiView.as_view(),name='best-selling-product'),
]