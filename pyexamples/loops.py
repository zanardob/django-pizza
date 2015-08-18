orders = [
    {
        'name': 'Mario',
        'flavor': 'pepperoni'
    },
    {
        'name': 'Marcolino',
        'flavor': 'barbecue'
    }
]

for order in orders:
    s = 'Name: {0}, Flavor: {1}'
    print(s.format(order['name'], order['flavor']))

