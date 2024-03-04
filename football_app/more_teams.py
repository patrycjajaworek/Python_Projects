import requests
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import parser

team_ids = [64]
headers = {'X-Auth-Token': '3ad4f0e78eeb410a9d851bc582a94619'}

for team_id in team_ids:
    plt.figure(figsize=(15, 6))

    uri = f'https://api.football-data.org/v2/teams/{team_id}/matches'
    response = requests.get(uri, headers=headers)

    if response.status_code == 200:
        matches_data = response.json()['matches']

        team_name = matches_data[0]['homeTeam']['name']

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
                    print(f"Nie można znaleźć drużyny {team_name} w meczu o ID: {match['id']}")
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

        plt.plot(matchdays, results, marker='o', linestyle='-', label=team_name)

        plt.xticks(matchdays)
        plt.title(f'Wyniki meczów {team_name}')
        plt.xlabel('Kolejka')
        plt.ylabel('Wynik meczu')
        plt.yticks([2.0, 1.0, 0.0], ['Wygrana', 'Remis', 'Porażka'])
        plt.legend()
        plt.grid(True)
        plt.show()

    else:
        print(f"Błąd zapytania HTTP dla drużyny o ID {team_id}: {response.status_code}")
