import requests
from difflib import SequenceMatcher
from datetime import datetime
from dateutil import parser
import matplotlib.pyplot as plt


headers = {'X-Auth-Token': '3ad4f0e78eeb410a9d851bc582a94619'}
uri = 'https://api.football-data.org/v2/competitions/PL/teams'
uri_base = 'https://api.football-data.org/v2/teams/{team_id}/matches'
teams={}
response = requests.get(uri, headers=headers)

def get_teams():
    uri = 'https://api.football-data.org/v2/competitions/PL/teams'
    response = requests.get(uri, headers=headers)
    teams = {}

    if response.status_code == 200:
        teams_data = response.json()['teams']
        for team in teams_data:
            team_id = team['id']
            team_name = team['name']
            formatted_team_name = team_name.replace(" fc", " FC").replace("Fc", "FC").replace("FC", "FC")
            teams[formatted_team_name.lower()] = team_id
            print(f"ID: {team_id}, Nazwa: {formatted_team_name}")
    else:
        print(f"Błąd zapytania HTTP: {response.status_code}")



for team_id, team_name in teams.items():
    uri = uri_base.format(team_id=team_id)
    team_name_str = team_name
    #print(f"\nURI dla drużyny {team_name}: {uri}")
    #print(f"Zmienna team_name: {team_name_str}")


def find_team_info(user_input):
    headers = {'X-Auth-Token': '3ad4f0e78eeb410a9d851bc582a94619'}
    uri_base = 'https://api.football-data.org/v2/teams/{team_id}/matches'

    teams = {}
    response = requests.get('https://api.football-data.org/v2/competitions/PL/teams', headers=headers)

    if response.status_code == 200:
        teams_data = response.json()['teams']
        for team in teams_data:
            team_id = team['id']
            team_name = team['name']
            formatted_team_name = team_name.replace(" fc", " FC").replace("Fc", "FC").replace("FC", "FC")
            teams[formatted_team_name.lower()] = {'id': team_id, 'name': formatted_team_name, 'formatted_v2': formatted_team_name}
            #print(f"ID: {team_id}, Nazwa: {formatted_team_name}")

    else:
        print(f"Błąd zapytania HTTP: {response.status_code}")
        return None

    #print("Słownik drużyn:", teams)

    best_match_ratio = 0
    best_match_team = None

    for team_name, team_info in teams.items():
        match_ratio = SequenceMatcher(None, user_input, team_name).ratio()
        if match_ratio > best_match_ratio:
            best_match_ratio = match_ratio
            best_match_team = team_name

    if best_match_ratio > 0.5:
        team_info = teams[best_match_team]
        team_id = team_info['id']
        formatted_team_name = team_info['name'].capitalize()
        formatted_team_name_v2 = team_info['formatted_v2']
        uri = uri_base.format(team_id=team_id)

        dictionary_teams = {
            'id': team_id,
            'team_name': formatted_team_name_v2,
        }

        #print(f"\nURI dla drużyny {formatted_team_name_v2}: {uri}")
        return dictionary_teams
    else:
        print(f"Nie można odnaleźć pasującej drużyny. Spróbuj ponownie.")
        return None
    return formatted_team_name_v2,uri






headers = { 'X-Auth-Token': '3ad4f0e78eeb410a9d851bc582a94619' }
today_date = datetime.now().date()


def get_matches_info(team_info):

    for match in matches_data:
        #print(match)
        competition_name = match['competition']['name']
        #print(competition_name)
        if competition_name == "Premier League":
            match_date = parser.parse(match['utcDate']).date()
            if today_date >= match_date:
                match_day = match['season']['currentMatchday']
                match_date = match['utcDate']
                home_team = match['homeTeam']['name']
                away_team = match['awayTeam']['name']
                match_result = f"{home_team} {match['score']['fullTime']['homeTeam']} : {match['score']['fullTime']['awayTeam']} {away_team}"

                print(f"Mecz dnia {match_date} pomiędzy {home_team} a {away_team} zakończył się wynikiem: {match_result}")
        else:
            continue
    return matches_data


def plot_form_chart(matches_data, team_name_is):
    matchdays = []
    results = []
    match_day = 0
    team_name = team_info['team_name']

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
                    print(f"Nie można znaleźć drużyny {team_info['team_name']} w meczu o ID: {match['id']}")
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
        else:
            continue

    plt.figure(figsize=(15, 6))
    plt.plot(matchdays, results, marker='o', linestyle='-', color='b')
    plt.xticks(matchdays)
    plt.title(f'Wyniki meczów {team_name}')
    plt.xlabel('Kolejka')
    plt.ylabel('Wynik meczu')
    plt.yticks([2.0, 1.0, 0.0], ['Wygrana', 'Remis', 'Porażka'])
    plt.grid(True)
    plt.show()


user_input = input("Which team do you want to check?: ").lower()
team_info = find_team_info(user_input)
team_id = team_info['id']
uri_team = f'https://api.football-data.org/v2/teams/{team_id}/matches'
response = requests.get(uri_team, headers=headers)
matches_data = response.json()['matches']
get_matches_info(team_info)

plot_form_chart(matches_data,team_info)
if team_info:
    print(f"Informacje o drużynie: {team_info}")

print(team_info['id'])
print(team_info['team_name'])



