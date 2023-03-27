#https://www.coingecko.com/en/api
import requests
import json

bob = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd',headers={"accept": "application/json"})
print("The price of bitcoin is currently: "+ str(bob.json()['bitcoin']['usd']))