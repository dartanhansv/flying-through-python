

# First, manually print each line item from the file
'''
def read_dollar_menu():
    dollar_spam = open('dollar_menu.txt', 'r')
    print('1st line: ', dollar_spam.readline())
    print('2nd line: ', dollar_spam.readline())
    dollar_spam.close()


# 2nd, user loop print all lines
def read_dollar_menu():
    dollar_spam = open('dollar_menu.txt', 'r')

    for line in dollar_spam:
        print(line)

    dollar_spam.close()    
'''

# 3rd, adding line items from the file to a list 
def read_dollar_menu():
    dollar_spam = open('dollar_menu.txt', 'r')
    # create an empty list
    dollar_menu = []
    
    for line in dollar_spam:
        dollar_menu.append(line)
    
    print(dollar_menu)
    dollar_spam.close()  


# Main function 
def main():
    read_dollar_menu()


main()