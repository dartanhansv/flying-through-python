

'''
def read_dollar_menu():
    dollar_spam = open('dollar_menu.txt', 'r')
    print('1st line: ', dollar_spam.readline())
    print('2nd line: ', dollar_spam.readline())
    dollar_spam.close()
'''


def read_dollar_menu():
    dollar_spam = open('dollar_menu.txt', 'r')

    for line in dollar_spam:
        print(line)

    dollar_spam.close()    



def main():
    read_dollar_menu()


main()