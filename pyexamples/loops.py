orders = [
    {
        'name': 'Mario',
        'flavor': 'pepperoni'
    },
    {
        'name': 'Marco',
        'flavor': 'ham'
    }
]

for order in orders:
    print('Name: {0}, Flavor: {1}'.format(order['name'], order['flavor']))
