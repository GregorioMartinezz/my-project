import requests


def suma(num1, num2):
    url = "https://faas-fra1-afec6ce7.doserverless.co/api/v1/web/fn-1f1056ff-de8e-4509-9811-27a68419f504/default/add"
    data = {'a':num1,'b':num2}
    headers = {'Content-Type': 'application/json'}
    return requests.post(url, headers = headers, json = data)

def test_suma(a, b):
    return int(suma(a, b).json()['result'])

response = suma(1, 3)
print('STATUS:  ', response.status_code)
print('RESPONSE:', response.text)
print('JSON', response.json() )
print('Suma', response.json()['result'])

assert test_suma(1, 3) == 4
assert test_suma(-1, -3) == -4


