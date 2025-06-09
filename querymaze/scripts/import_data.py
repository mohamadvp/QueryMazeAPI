import csv
from querymaze.models import Product, Customer, Order, OrderItem
from datetime import datetime
from django.db import transaction


def import_data():
    try:
        with transaction.atomic():
            with open("/home/mohammad/Downloads/noahs-csv/5784/noahs-products.csv") as f:
                print("Importing products...")
                reader = csv.DictReader(f)
                for row in reader:
                    Product.objects.create(
                        sku=row['sku'],
                        desc=row['desc'],
                        wholesale_cost=row['wholesale_cost'],
                        dims_cm=row['dims_cm'],
                    )
            with open("/home/mohammad/Downloads/noahs-csv/5784/noahs-customers.csv") as f:
                print("Importing customers...")
                reader = csv.DictReader(f)
                for row in reader:
                    Customer.objects.create(
                        customerid=row["customerid"],
                        name=row["name"],
                        address=row["address"],
                        citystatezip=row["citystatezip"],
                        birthdate=datetime.strptime(
                            row["birthdate"], "%Y-%m-%d"),
                        phone=row["phone"],
                        timezone=row["timezone"],
                        lat=float(row["lat"]),
                        long=float(row["long"]),
                    )
            with open("/home/mohammad/Downloads/noahs-csv/5784/noahs-orders.csv") as f:
                print("Importing orders...")
                reader = csv.DictReader(f)
                for row in reader:
                    Order.objects.create(
                        orderid=row["orderid"],
                        customer=Customer.objects.get(
                            customerid=row["customerid"]),
                        ordered=datetime.strptime(
                            row["ordered"], "%Y-%m-%d %H:%M:%S"),
                        shipped=datetime.strptime(
                            row["shipped"], "%Y-%m-%d %H:%M:%S"),
                        items=row["items"],
                        total=row["total"],
                    )
            with open("/home/mohammad/Downloads/noahs-csv/5784/noahs-orders_items.csv") as f:
                print("Importing orders item...")
                reader = csv.DictReader(f)
                for row in reader:
                    OrderItem.objects.create(
                        order=Order.objects.get(orderid=row["orderid"]),
                        product=Product.objects.get(sku=row["sku"]),
                        qty=int(row["qty"]),
                        unit_price=float(row["unit_price"]),
                    )

    except Exception as e:
        print("Error:", e)
        return {"error": str(e)}
