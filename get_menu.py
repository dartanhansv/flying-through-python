import requests

my_request = requests.get('http://go.codeschool.com/spamvanmenu')

menu_list = my_request.json() 

print(menu_list)