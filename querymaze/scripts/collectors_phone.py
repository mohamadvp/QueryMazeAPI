from django.db.models import Count,Q
from querymaze.models import Customer

def find_collector():
    print("Looking for the Collector...")

    collectors = Customer.objects.annotate(col_count =Count('order__orderitem__product',
    filter=Q(order__orderitem__product__sku__startswith='COL'),
    distinct=True
    )
    ).order_by('-col_count').first()

    if collectors and collectors.col_count > 0 :
        print(f'The Collector name: {collectors.name} - phone:{collectors.phone}')
    else:
        print("No match found...")  