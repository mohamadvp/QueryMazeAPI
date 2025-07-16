from django.db.models import F, ExpressionWrapper, DecimalField
from querymaze.models import Customer, OrderItem


def find_cousin():
    print("Looking for the cousin...")

    items = OrderItem.objects.annotate(profit=ExpressionWrapper(
        F('qty') * (F('unit_price') - F('product__wholesale_cost')),
        output_field=DecimalField(max_digits=20, decimal_places=3)
    ))

    customer_profits = {}

    for item in items.select_related('order__customer', 'product'):
        customer = item.order.customer
        customer_profits.setdefault(customer,0)
        customer_profits[customer] += item.profit


    sorted_customer = sorted(customer_profits.items(), key=lambda x: x[1])

    if sorted_customer:
        customer, profit = sorted_customer[0]
        print(f"The Cousin name: {customer.name} - phone: {customer.phone}")
        return (item, customer)
    else:
        print('No match found...')