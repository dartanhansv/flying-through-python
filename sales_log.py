
order = {'Cheeky Spam': 1.0, 'Yonks Spam': 4.0}

def write_sales_log(order):
    # open the file
    file = open('sales.txt', 'w')

    # write each item to the file
    # write the total to the file
    for order in order:
        file.write(order+'\n')


    # close the file
    file.close()