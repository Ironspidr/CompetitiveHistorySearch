import json
import requests

history = requests.get(
    'https://www.nj-web.com/pubDB/CompetitiveHistory.json').json()


full_history = json.loads(history)

print(full_history[0]['2023'])
