from django.urls import path, include

urlpatterns = [
path('',include('querymaze.urls.orderUrls')),
path('',include('querymaze.urls.customerUrls')),
path('',include('querymaze.urls.reportUrls')),
path('',include('querymaze.urls.productUrls')),
]