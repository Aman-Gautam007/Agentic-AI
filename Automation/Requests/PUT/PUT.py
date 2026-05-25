import requests

res = requests.put('https://httpbin.org/put', data={'key': 'value'})

print("Status Code:", res.status_code)

print("Response Body:", res.content.decode())