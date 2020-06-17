from urllib.parse import urlencode
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

token = "042b4bc0701d5416293bb221df2a95a7d6cb7596c21963e8b1245dadd8cb35ca64c8dc8588b0f785512c5"

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

        return results

    def print(self):
        line = 'https://vk.com/id'
        print(line+self.id)

olga = Users('109633595', token)
veronika = Users('3869695', token)

for values in olga & veronika:
    values.print()

