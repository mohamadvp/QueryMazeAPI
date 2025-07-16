from querymaze.models import Customer

t9 = {
    'A': '2', 'B': '2', 'C': '2',
    'D': '3', 'E': '3', 'F': '3',
    'G': '4', 'H': '4', 'I': '4',
    'J': '5', 'K': '5', 'L': '5',
    'M': '6', 'N': '6', 'O': '6',
    'P': '7', 'Q': '7', 'R': '7', 'S': '7',
    'T': '8', 'U': '8', 'V': '8',
    'W': '9', 'X': '9', 'Y': '9', 'Z': '9',
}


def name_to_number(name: str) -> str:
    return ''.join(t9.get(char.upper(), '') for char in name if name.isalpha())


def find_investigator():
    print("Looking for the phone number of investigator ...")

    for customer in Customer.objects.all():
        name_parts = customer.name.split()
        last_name = name_parts[-1]
        name_digits = name_to_number(last_name)
        phone_digits = ''.join(c for c in customer.phone if c.isdigit())
        if phone_digits == name_digits:
            print(f'The investigator found: {customer.name} - phone:{customer.phone}')
            return

    print('No match found...')
