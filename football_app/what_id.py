import requests

headers = {'X-Auth-Token': '3ad4f0e78eeb410a9d851bc582a94619'}
uri = 'https://api.football-data.org/v2/competitions/PL/teams'
uri_base = 'https://api.football-data.org/v2/teams/{team_id}/matches'
teams={}
response = requests.get(uri, headers=headers)

if response.status_code == 200:
    teams_data = response.json()['teams']
    for team in teams_data:
        team_id = team['id']
        team_name = team['name']
        teams[team_id] = team_name
        print(f"ID: {team_id}, Nazwa: {team_name}")


else:
    print(f"Błąd zapytania HTTP: {response.status_code}")

print("Słownik drużyn:", teams)

for team_id, team_name in teams.items():
    uri = uri_base.format(team_id=team_id)
    team_name_str = team_name
    print(f"\nURI dla drużyny {team_name}: {uri}")
    print(f"Zmienna team_name: {team_name_str}")