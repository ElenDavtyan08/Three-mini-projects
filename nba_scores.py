from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"  # "https://cdn.nba.com"
ALL_JSON = "/prod/v1/today.json" # "/static/json/liveData/scoreboard/todaysScoreboard_00.json"

printer = PrettyPrinter()

def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links

def get_scoreboard():
    screboard = get_links()['currentScoreboard']
    games = get(BASE_URL + screboard).json()['games']

    for game in games:
        home_team = game['hTeam']
        away_taem = game['vTeam']
        clock = game['clock']
        period = game['period']

        print('----------------------------------------------')
        print(f"{home_team['triCode']} vs {away_taem['triCode']}")
        print(f"{home_team['score']} - {away_taem['score']}")
        print(f"{clock} - {period['current']}")

def get_stats():
    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']

    teams = list(filter(lambda x: x['name'] != "Team", teams))
    teams.sort(key=lambda x: int(x['ppg']['rank']))

    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']
        print(f"{i + 1}. {name} - {nickname} - {ppg}")


get_stats()
