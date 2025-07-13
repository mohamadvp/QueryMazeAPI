from querymaze.models import Customer, Order, OrderItem

def run():
    print("Looking for the Cat Lady...")

    for customer in Customer.objects.filter(citystatezip__icontains='Staten Island'):
        orders = Order.objects.filter(customer=customer)
        items = OrderItem.objects.filter(order__in=orders, qty__gte=10).values_list('product__desc',flat=True)
        if any('cat' in desc.lower() for desc in items):
            print(f"The Cat Lady {customer.name} - phone: {customer.phone}")
            return
    print("No match found.")
