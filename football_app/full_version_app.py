import requests
from difflib import SequenceMatcher
from datetime import datetime
from dateutil import parser
import matplotlib.pyplot as plt

headers = {'X-Auth-Token': '3ad4f0e78eeb410a9d851bc582a94619'}
uri_base = 'https://api.football-data.org/v2/teams/{team_id}/matches'

def get_teams():
    uri = 'https://api.football-data.org/v2/competitions/PL/teams'
    response = requests.get(uri, headers=headers)
    teams = {}

    if response.status_code == 200:
        teams_data = response.json()['teams']
        for team in teams_data:
            team_id = team['id']
            team_name = team['name'].replace(" fc", " FC").replace("Fc", "FC").replace("FC", "FC")

            teams[team_name.lower()] = team_id
    else:
        print(f"Błąd zapytania HTTP: {response.status_code}")
        return None

    return teams

def find_team_info(user_input, teams):
    best_match_ratio = 0
    best_match_team = None

    for team_name, team_id in teams.items():
        match_ratio = SequenceMatcher(None, user_input, team_name).ratio()
        if match_ratio > best_match_ratio:
            best_match_ratio = match_ratio
            best_match_team = team_name

    if best_match_ratio > 0.5:
        team_id = teams[best_match_team]
        formatted_team_name = best_match_team.capitalize()
        #formatted_team_name = formatted_team_name.replace("fc","FC")
        uri = uri_base.format(team_id=team_id)

        dictionary_teams = {'id': team_id, 'team_name': formatted_team_name}
        print(f"\nURI dla drużyny {formatted_team_name}: {uri}")
        return dictionary_teams
    else:
        print(f"Nie można odnaleźć pasującej drużyny. Spróbuj ponownie.")
        return None

def get_matches_info(team_info):
    uri_team = f'https://api.football-data.org/v2/teams/{team_info["id"]}/matches'
    today_date = datetime.now().date()
    response = requests.get(uri_team, headers=headers)
    matches_data = response.json()['matches']

    for match in matches_data:
        competition_name = match['competition']['name']
        if competition_name == "Premier League":
            match_date = parser.parse(match['utcDate']).date()
            if today_date >= match_date:
                home_team = match['homeTeam']['name']
                away_team = match['awayTeam']['name']
                match_result = f"{home_team} {match['score']['fullTime']['homeTeam']} : {match['score']['fullTime']['awayTeam']} {away_team}"

                print(f"Mecz dnia {match_date} pomiędzy {home_team} a {away_team} zakończył się wynikiem: {match_result}")
    return matches_data

def plot_results(matches_data, team_name):
    matchdays = []
    results = []
    match_day = 0

    today_date = datetime.now().date()
    for match in matches_data:
        competition_name = match['competition']['name']

        if competition_name == "Premier League":
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
                    result = 1.0 if winner == 'DRAW' else 2.0 if winner == team else 0.0
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

if __name__ == "__main__":
    teams = get_teams()

    if teams:
        user_input = input("Which team do you want to check?: ").lower()
        team_info = find_team_info(user_input, teams)

        if team_info:
            print(f"Informacje o drużynie: {team_info}")
            matches_data = get_matches_info(team_info)
            plot_results(matches_data, team_info['team_name'])
