import requests


url = 'https://www.nba.com/stats/leaders?SeasonType=Regular%20Season'
r = requests.get(url)
# print(r.text)

with open('nba.html', 'wb+') as fd:
    fd.write(r.content)


