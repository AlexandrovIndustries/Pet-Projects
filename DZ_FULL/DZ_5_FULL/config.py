import requests

TOKEN = "73**********:AAEn4dzJeaTdM******************"

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
response = requests.get(url)
print(response.json())