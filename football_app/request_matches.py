import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import parser
team_id = 64
#uri = 'https://api.football-data.org/v2/teams/64/matches'  # ID 64 odpowiada Liverpoolowi
uri = f'https://api.football-data.org/v2/teams/{team_id}/matches'
headers = { 'X-Auth-Token': '3ad4f0e78eeb410a9d851bc582a94619' }

response = requests.get(uri, headers=headers)
matches_data = response.json()['matches']

name = matches_data[0]['homeTeam']['name']
print(name)
team_name = "Liverpool FC"
#team_name=""

for match in matches_data:
    match_day = match['matchday']
    match_date = match['utcDate']
    home_team = match['homeTeam']['name']
    away_team = match['awayTeam']['name']
    match_result = f"{home_team} {match['score']['fullTime']['homeTeam']} : {match['score']['fullTime']['awayTeam']} {away_team}"

    print(f"Mecz dnia {match_date} pomiędzy {home_team} a {away_team} zakończył się wynikiem: {match_result}")
    #print(match)

matchdays = []
results = []
today_date = datetime.now().date()
match_day = 0



for match in matches_data:
    match_date = parser.parse(match['utcDate']).date()

    if match_date < today_date:
        match_day += 1
        matchdays.append(match_day)
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']

        if home_team == team_name:
            team = 'HOME_TEAM'
        elif away_team == team_name:
            team = 'AWAY_TEAM'
        else:
            print(f"Nie można znaleźć drużyny Liverpoolu w meczu o ID: {match['id']}")
            break

        if 'score' in match and 'winner' in match['score']:
            winner = match['score']['winner']
            if winner == 'DRAW':
                result = 1.0
            elif winner == team:
                result = 2.0
            else:
                result = 0.0
            results.append(result)
        else:
            print(f"Nie można znaleźć wyniku dla meczu o ID: {match['id']}")
            break

plt.figure(figsize=(15, 6))
plt.plot(matchdays, results, marker='o', linestyle='-', color='b')
plt.xticks(matchdays)
plt.title(f'Wyniki meczów {team_name}')
plt.xlabel('Kolejka')
plt.ylabel('Wynik meczu')
plt.yticks([2.0, 1.0, 0.0], ['Wygrana', 'Remis', 'Porażka'])
plt.grid(True)
plt.show()


