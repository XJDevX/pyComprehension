#<--Filtros para diccionarios con lambda y filter()-->#

matches = [
    {
        'home_team': 'Bolivia',
        'away_team': 'Uruguay',
        'home_team_score': 1,
        'away_team_score': 3,
        'home_team_result': 'Lose'
    },
    {
        'home_team': 'Brazil',
        'away_team': 'Mexico',
        'home_team_score': 1,
        'away_team_score': 1,
        'home_team_result': 'Draw'
    },
    {
        'home_team': 'Ecuador',
        'away_team': 'Venezuela',
        'home_team_score': 5,
        'away_team_score': 0,
        'home_team_result': 'Win'
    },
]

print(matches)
print(len(matches))

matchResults = list(
    filter(lambda item: item["home_team_result"] == "Win", matches))

print(f"Partidos ganados: {matchResults}")
print(len(matchResults))