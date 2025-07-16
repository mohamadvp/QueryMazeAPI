from datetime import timedelta
from querymaze.models import Customer, Order, OrderItem
from .neighbor_phone import find_neighbor

def find_bicycleFixer():
    neighbor = find_neighbor()
    print("Looking for the phone number of bicycle fixer ...")

    for customer in Customer.objects.exclude(customerid=neighbor.customerid):
        orders = Order.objects.filter(customer = customer)

        for order in orders:
            if order.ordered.time().hour != 4:
                continue
            item = OrderItem.objects.filter(order=order).values_list('product__desc',flat=True)
            time_diff = order.shipped - order.ordered
            if any('bagel' in desc.lower() for desc in item) and  time_diff <= timedelta(minutes=10):
                print(f" The bicycle fixer {customer.name} - phone:{customer.phone}")    
                return
    print('No match found...')
