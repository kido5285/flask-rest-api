import requests

base_url = 'http://127.0.0.1:5000'

data = [{'name': 'tutorial0', 'likes': 3298932, 'views': 3344353543}
        ,{'name': 'tutorial1', 'likes': 345435456, 'views': 2345345435}
        ,{'name': 'tutorial2', 'likes': 5464566456, 'views': 3344643453353543}
        ,{'name': 'tutorial3', 'likes': 3295435438932, 'views': 334453453353543}
        ,{'name': 'tutorial4', 'likes': 3295345348932, 'views': 3344657563657553543}]


resp = requests.put(base_url + '/video/0', data[0])
print(resp)

resp2 = requests.get(base_url + '/video/0')
print(resp2)

# resp=requests.delete(base_url + '/video/0')
# print(resp)