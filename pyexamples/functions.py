orders = []


def add_order(name, flavor, optionals=None):
    order = {}
    order['name'] = name
    order['flavor'] = flavor
    order['optionals'] = optionals

    return order

orders.append(add_order('Mario', 'Pepperoni'))
orders.append(add_order('Marcolino', 'Barbecue', 'Toasted'))

for order in orders:
    if order['optionals']:
        template = 'Name: {name}\nFlavor: {flavor}\nOptionals: {optionals}'
    else:
        template = 'Name: {name}\nFlavor: {flavor}'

    print(template.format(**order))
    print('-' * 80)
