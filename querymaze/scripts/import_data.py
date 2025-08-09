import environ
import os
import csv
from querymaze.models import Product, Customer, Order, OrderItem
from datetime import datetime
from django.utils import timezone
from django.db import transaction

env = environ.Env()
environ.Env.read_env()

def import_data():
    try:
        with transaction.atomic():
            with open(env("PRODUCT_CSV")) as f:
                print("Importing products...")
                reader = csv.DictReader(f)
                for row in reader:
                    Product.objects.update_or_create(
                        sku=row['sku'],
                        desc=row['desc'],
                        wholesale_cost=row['wholesale_cost'],
                        dims_cm=row['dims_cm'],
                    )
            with open(env("CUSTOMER_CSV")) as f:
                print("Importing customers...")
                reader = csv.DictReader(f)
                for row in reader:
                    Customer.objects.update_or_create(
                        customerid=row["customerid"],
                        name=row["name"],
                        address=row["address"],
                        citystatezip=row["citystatezip"],
                        birthdate=datetime.strptime(row["birthdate"], "%Y-%m-%d"),
                        phone=row["phone"],
                        timezone=row["timezone"],
                        lat=float(row["lat"]),
                        long=float(row["long"]),
                    )
            with open(env("ORDER_CSV")) as f:
                print("Importing orders...")
                reader = csv.DictReader(f)
                for row in reader:
                    Order.objects.update_or_create(
                        orderid=row["orderid"],
                        defaults={
                            'customer': Customer.objects.get(customerid=row["customerid"]),
                            'ordered': timezone.make_aware(datetime.strptime(row["ordered"], "%Y-%m-%d %H:%M:%S")),
                            'shipped': timezone.make_aware(datetime.strptime(row["shipped"], "%Y-%m-%d %H:%M:%S")),
                            'items': row["items"],
                            'total': row["total"],
                        }
                    )
            with open(env("ORDERITEM_CSV")) as f:
                print("Importing orders item...")
                reader = csv.DictReader(f)
                for row in reader:
                    OrderItem.objects.update_or_create(
                        order=Order.objects.get(orderid=row["orderid"]),
                        product=Product.objects.get(sku=row["sku"]),
                        qty=int(row["qty"]),
                        unit_price=float(row["unit_price"]),
                    )

    except Exception as e:
        print("Error:", e)
        return {"error": str(e)}
