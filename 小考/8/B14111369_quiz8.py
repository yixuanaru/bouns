import csv

# Read the CSV file
with open('pe8_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# (1) Eastern teams with home win% < away win%
print("Eastern teams with home win% < away win%:")
for row in data:
    if row['Conference'] == 'Eastern':
        home_win_pct = float(row['HOME'].split('-')[0]) / (float(row['HOME'].split('-')[0]) + float(row['HOME'].split('-')[1]))
        away_win_pct = float(row['AWAY'].split('-')[0]) / (float(row['AWAY'].split('-')[0]) + float(row['AWAY'].split('-')[1]))
        if home_win_pct < away_win_pct:
            print(row['Team'])
print()

# (2) Conference with higher average "PF - PA"
east_pf_pa_diff = 0
east_team_count = 0
west_pf_pa_diff = 0
west_team_count = 0

for row in data:
    if row['Conference'] == 'Eastern':
        east_pf_pa_diff += float(row['PF']) - float(row['PA'])
        east_team_count += 1
    else:
        west_pf_pa_diff += float(row['PF']) - float(row['PA'])
        west_team_count += 1

east_avg_pf_pa_diff = east_pf_pa_diff / east_team_count
west_avg_pf_pa_diff = west_pf_pa_diff / west_team_count

print("Conference with higher average 'PF - PA':")
if east_avg_pf_pa_diff > west_avg_pf_pa_diff:
    print("Eastern Conference")
else:
    print("Western Conference")
print()

# (3) Ranking based on win% against other conference
teams_sorted = sorted(data, key=lambda x: float(x['CONF'].split('-')[0]) / (float(x['CONF'].split('-')[0]) + float(x['CONF'].split('-')[1])), reverse=True)

print("Ranking based on win% against other conference:")
rank = 1
for team in teams_sorted:
    print(f"{rank}. {team['Team']} ({team['CONF']})")
    rank += 1