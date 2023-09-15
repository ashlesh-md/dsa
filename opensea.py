import requests

url = "https://testnets-api.opensea.io/v2/orders/goerli/seaport/listings?limit=1"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
