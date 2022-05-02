import base64
import datetime
import json

import requests


def send_to_email(receiver, filename):
    if len(receiver) == 0:
        print("Email Skipped")
        return
    print("Sending email...")

    data = open(filename, "rb").read()
    encoded = base64.b64encode(data)

    url = "https://emailapi.netcorecloud.net/v5/mail/send"

    payload = '{"from": {"email": "cedricringger@pepisandbox.com","name": "cedricringger"},"subject": "Report ' + filename + '","content": [{"type": "html","value": "This report was Created at ' + datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + '"}],"attachments":[{"content": "' + encoded.decode("utf-8") + '","type": "application/pdf"}],"personalizations": [{"to": [{"email": "' + receiver + '","name": "Lionel Messi"}]}]}'
    headers = {'api_key': "0fb8a6e67439229ac3cc9ded737d017b", 'content-type': "application/json"}

    response = requests.request("POST", url, data=payload, headers=headers)
    data = json.loads(response.text)
    if "error" in data:
        print("Sending Email failed")
        return
    print("Done...")
