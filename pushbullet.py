import requests
import json


class Pushbullet():

    def __init__(self):
        self.HEADER = {
            'Access-Token': 'o.F8g1gAj8DtS1LEExYux7UQycVVwfp9Qk',
            'Content-Type': 'application/json'
        }
        self.ME_API = 'https://api.pushbullet.com/v2/users/me'
        self.PUSH_API = 'https://api.pushbullet.com/v2/pushes'

    def send_note(self, title, body):
        data = {
            'title': title,
            'body': body,
            'type': 'note'
        }

        r = requests.post(
            self.PUSH_API,
            headers=self.HEADER,
            data=json.dumps(data)
        )

        print(r.status_code)
        print(r.json())
