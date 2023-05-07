import orders




def main():
    menu = {'Knackered Spam': 0.50, 'Pip pip Spam': 1.50, 'Squidgy Spam': 2.50, 'Smashing Spam':3.50}
    print_menu(menu)
    order = get_order(menu)
    total = bill_total(order, menu)
    print("You ordered: ", order, "\n", "Your total is: $", format(total, '.2f'), sep='')
main()