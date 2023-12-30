import json
import requests

# Returns list of competitors from a given year and event


def getCompetitors(conf):
    competitors = []
    for i in conf:
        if isinstance(i['Competitor(s)'], list):
            for j in i['Competitor(s)']:
                competitors.append(j)
        else:
            competitors.append(i['Competitor(s)'])

    competitors = list(dict.fromkeys(competitors))

    print(competitors)

# Returns dict of competitors from a given year and event


def getEvents(conf):
    comp_dict = dict()

    for i in conf:

        x = i['Event']
        y = i['Competitor(s)']

        comp_dict[x] = y

    return comp_dict


history = requests.get(
    'https://www.nj-web.com/pubDB/CompetitiveHistory.json').json()


chooseYear = input('Enter the year: ')

result = history[chooseYear]

chooseEvent = int(input('Enter the event [2] - ISLC, [1] - SLC, [0] - NLC: '))

result_conf = (result[chooseEvent])['ISLC']

# getCompetitors(result_conf)
# getEvents(result_conf)
