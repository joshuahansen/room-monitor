"""
Author: Joshua Hansen
Student Number: s3589185
Email: s3589185@student.rmit.edu.au

Programming Interrnet of Things COSC2674
Semester 2, 2018
Assignment 1

This module was written to interact with the pushbullet api
It is intended to be run with python 3 and is used as part
of Assignement 1 for the course
"""
import json
import requests


class Pushbullet:
    """
    Pushbullet class for handeling all interaction with the
    pushbullet api
    """

    def __init__(self):
        """Constructor to create API header and URLs"""
        self.header = {
            'Access-Token': 'o.F8g1gAj8DtS1LEExYux7UQycVVwfp9Qk',
            'Content-Type': 'application/json'
        }
        self.push_api = 'https://api.pushbullet.com/v2/pushes'

    def send_note(self, title, body):
        """Create api json and post to api endpoint"""
        data = {
            'title': title,
            'body': body,
            'type': 'note'
        }

        req = requests.post(
            self.push_api,
            headers=self.header,
            data=json.dumps(data)
        )

        print(req.status_code)
        print(req.json())
