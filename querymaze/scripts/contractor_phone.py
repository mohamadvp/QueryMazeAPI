from querymaze.models import Order, Customer, OrderItem


def find_contractor():
    print("Looking for the phone number of contractor ...")

    customers = Customer.objects.filter(
        name__regex=r'^J.*\sP.*'
    )
    orders = Order.objects.filter(customer__in=customers, ordered__year=2017)
    item = OrderItem.objects.filter(order__in=orders, product__desc__icontains='coffee').first()
    if item:
        print(f"The Contractor found:  {item.order.customer.name} phone - {item.order.customer.phone}")
        return item.order.customer
    else:
        print('No match found...')
