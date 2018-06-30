
import requests

r = requests.post('http://127.0.0.1:3000/user/add', data={
    'username': 'gua1111',
    'xfrs': '066e3ec5-c50d-44e8-b04d-a8da45bd87ae',
})

print(r, r.text)