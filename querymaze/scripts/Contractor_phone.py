from querymaze.models import Order, Customer, OrderItem


def run():
    print("Looking for the phone number of contractor ...")

    customers = Customer.objects.filter(
        name__regex=r'^J.*\sP.*'
    )

    for customer in customers:
        orders = Order.objects.filter(customer=customer, ordered__year=2017)
        for order in orders:
            item = OrderItem.objects.filter(order=order).values_list('product__desc', flat=True)
            if any('coffee' in desc.lower() for desc in item):
                print(f"The Contractor found:  {customer.name} phone - {customer.phone}")
                return
        
    print("No Matching ...")
