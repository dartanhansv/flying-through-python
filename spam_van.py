import orders




def main():
    menu = {'Knackered Spam': 0.50, 'Pip pip Spam': 1.50, 'Squidgy Spam': 2.50, 'Smashing Spam':3.50}
    # we need to add orders before each of the functions that are part of the orders module
    orders.print_menu(menu)
    order = orders.get_order(menu)
    total = orders.bill_total(order, menu)
    print("You ordered: ", order, "\n", "Your total is: $", format(total, '.2f'), sep='')
main()