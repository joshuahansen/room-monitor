import pushbullet


class SendMessage():

    def __init__(self):
        try:
            api_key = "o.vYD3LggYwXoVGZd9jJdkyU9NfOffNoRs"
            self.pb = pushbullet.Pushbullet(api_key)
        except pushbullet.errors.InvalidKeyError:
            print("Please enter a valid Pushbullet api key")

    def send(self, title, message):
        try:
            self.pb.push_note(title, message)
        except AttributeError:
            print("Failed to connect to pushbullet api")


sm = SendMessage()
sm.send("Test", "This is a test message")
