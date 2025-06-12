from datetime import date
from querymaze.models import Customer
from .contractor_phone import find_contractor


CancerRabbitYear = [1915, 1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023]


def CancerDate(birthdate: date) -> bool:
    return (birthdate.month == 6 and birthdate.day >= 22) or (birthdate.month == 7 and birthdate.day <= 22)

def find_neighbor():
    contractor = find_contractor()
    if not contractor:
        print("No contractor found")
    citystatezip = contractor.citystatezip    

    print("Looking for the phone number of neighbor ...")

    customers = Customer.objects.filter(birthdate__year__in=CancerRabbitYear, citystatezip__icontains=citystatezip)

    for customer in customers:
        birthdate = customer.birthdate
        if not (CancerDate(birthdate)):
            continue
        print(f"The Neighbor found: {customer.name} - phone: {customer.phone}")
        return
    print("Not Match .....")
