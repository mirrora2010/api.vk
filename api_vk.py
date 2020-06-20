from urllib.parse import urlencode
from pprint import pprint
import requests

OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMs = {
    'client_id': 7512027,
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': 5.89
}

print('?'.join(
(OAUTH_URL, urlencode(OAUTH_PARAMs))
))

token = "cea56fcb248045b854fdb1c6477ca5a487ac6130a9c1500fde22a4a6df73fdd990de711fe795687c0c458"

url = 'https://api.vk.com/method/friends.getMutual'

class Users:
    def __init__(self, id=str, token=str) -> None:
        self.token = token
        self.id = id
        self.v = 5.91

    def __and__(self, object):
        params = {
            'source_uid': self.id,
            'access_token': self.token,
            'target_uid': object.id,
            'v': 5.91
        }

        results = []

        response = requests.get('https://api.vk.com/method/friends.getMutual', params)

        ids = response.json()['response']
        for values in ids:
            results.append(Users(str(values), token))
            print (f'Общий друг в сети VK: https://vk.com/id{values}')
        return results
    def __str__(self):
        return f'Ссылка на профиль пользователя в сети VK: https://vk.com/id{self.id}'

user1 = Users('109633595', token)
user2 = Users('3869695', token)

user1 & user2

print (user1)
print (user2)









