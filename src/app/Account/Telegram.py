import requests
TOKEN = '6091261455:AAEQ6ZZlLqkLYyNOOZkDpujQJ3dyLjAfzj8'
chat_id = "6210537537"
message = "Valoche est a la ramasse"
url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TOKEN, chat_id, message)

print(requests.get(url).json())