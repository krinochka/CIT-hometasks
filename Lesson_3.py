import requests as req
import json

headers = {'content-type': 'application/json'}
url = 'https://cit-home1.herokuapp.com/api/register'
data = {"Comment": "Hello from Karina M"}

r=req.post(url, data=json.dumps(data), headers=headers)

print(r)

r=req.get('https://cit-home1.herokuapp.com/api/check_me')

print(r.json())
