import requests
import json


history = requests.get(
    "https://www.nj-web.com/pubDB/tests.json").json()

history_2023 = history['2023']

nlc_2023 = history_2023['NLC']

event = nlc_2023[0]

print(event)
