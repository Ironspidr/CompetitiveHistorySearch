import json
import requests

history = requests.get(
    'https://www.nj-web.com/pubDB/CompetitiveHistory.json').json()


chooseYear = input('Enter the year: ')
# chooseEvent = input('Enter the event [1] for : ')
result = history[chooseYear]
