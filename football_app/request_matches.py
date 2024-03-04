import requests
from datetime import datetime
from dateutil import parser
import matplotlib.pyplot as plt
pl_teams=[]
def get_premier_league_teams():
    uri = 'https://api.football-data.org/v2/competitions/PL/teams'
    headers = {'X-Auth-Token': '3ad4f0e78eeb410a9d851bc582a94619'}

    response = requests.get(uri, headers=headers)
    teams_data = response.json()['teams']

    premier_league_teams = [team['name'] for team in teams_data]
    pl_teams.append([team['name'] for team in teams_data])
    return premier_league_teams,pl_teams

all_teams = get_premier_league_teams()
#print("Wszystkie zespoły Premier League:")
#for team in all_teams:
#    print(team)



print(pl_teams)





def generate_team_points(team_name):
    team_id_request_uri = f'https://api.football-data.org/v2/teams'
    headers = {'X-Auth-Token': '3ad4f0e78eeb410a9d851bc582a94619'}

    response = requests.get(team_id_request_uri, headers=headers)
    teams_data = response.json()['teams']

    team_id = None
    for team in teams_data:
        if team['name'] == team_name:
            team_id = team['id']
            break

    if team_id is None:
        print(f"Nie można znaleźć drużyny o nazwie {team_name}")
        return

    uri = f'https://api.football-data.org/v2/teams/{team_id}/matches'
    response = requests.get(uri, headers=headers)
    matches_data = response.json()['matches']

    team_points = {}

    today_date = datetime.now().date()
    match_day = 0

    for match in matches_data:
        match_date = parser.parse(match['utcDate']).date()

        if match_date < today_date:
            match_day += 1
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']

            if home_team == team_name:
                team = 'HOME_TEAM'
            elif away_team == team_name:
                team = 'AWAY_TEAM'
            else:
                print(f"Nie można znaleźć drużyny {team_name} w meczu o ID: {match['id']}")
                continue

            if 'score' in match and 'winner' in match['score']:
                winner = match['score']['winner']
                if winner == 'DRAW':
                    result = 1
                elif winner == team:
                    result = 3
                else:
                    result = 0

                team_points[home_team] = team_points.get(home_team, 0) + result
                team_points[away_team] = team_points.get(away_team, 0) + result
            else:
                print(f"Nie można znaleźć wyniku dla meczu o ID: {match['id']}")
                continue

    #sorted_teams = sorted(team_points.items(), key=lambda x: x[1], reverse=True)

    print(f"Liczba punktów dla {team_name} wynosi {team_points.get(team_name, 0)}")


list=[]
for team_data in pl_teams:
    for element in team_data:
        list.append(element)
        print(element)


for team in list:
    generate_team_points(team)



