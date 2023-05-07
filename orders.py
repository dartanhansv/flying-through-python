"""
1. Print the menu
2. Take an order
3. Calculate the total bill
"""

def print_menu(menu):
    for name, price in menu.items():
        print(name, ': $', format(price, '.2f'), sep="")

def get_order(menu):
    orders = []
    order = input("What would you like to order? (Q to Quit)")

    while (order.upper() != 'Q'):
        # find the order
        found = menu.get(order)
        if found:
            orders.append(order)
        else:
            print("Menu item doesn't exist")
        
        order = input('Anything else? (Q to Quit)')
    return orders


def bill_total(orders, menu):           # Parameters: we need the list of orders and the menu to look up the price
    total = 0

    for order in orders:                # Program Logic: For each order in our orders list, we want to add the price to our total
        total += menu[order]

    return total                        # Return the total


