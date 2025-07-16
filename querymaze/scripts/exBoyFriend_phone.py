from django.db.models import Q
from querymaze.models import Order, OrderItem
from .cousin_phone import find_cousin
import re

def normalize_desc(desc):
    return re.sub(r"\s*\(.*?\)", "", desc).strip().lower()

def find_exBoyfriend():
    item, cousin = find_cousin()
    order = Order.objects.filter(customer = cousin)
    items = OrderItem.objects.filter(order__in = order , product__sku__icontains="COL")

    filter = Q()
    for item in items :
        date = item.order.ordered.date()
        hour = item.order.ordered.hour
        product_desc = normalize_desc(item.product.desc)

        filter |= Q(
            order__ordered__date=date,
            order__ordered__hour=hour,
            product__desc__icontains=product_desc
        )

    matching_item = OrderItem.objects.filter(filter).exclude(order__customer = cousin).distinct()
    if matching_item:
        exBoyfriend = matching_item.first()
        print (f"The Ex boyfriend name: {exBoyfriend.order.customer.name} - phone: {exBoyfriend.order.customer.phone}")
    else:
        print('No match found...')