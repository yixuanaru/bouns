# Importing necessary libraries
import csv

# Reading the CSV file
with open('pe8_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Function to calculate win-loss percentage
def win_loss_percentage(wins, losses):
    total_games = wins + losses
    if total_games == 0:
        return 0
    return wins / total_games

# Question 1
eastern_teams_home_lower_away = []
for team in data:
    if team['Conference'] == 'Eastern':
        home_wins, home_losses = map(int, team['HOME'].split('-'))
        away_wins, away_losses = map(int, team['AWAY'].split('-'))
        home_pct = win_loss_percentage(home_wins, home_losses)
        away_pct = win_loss_percentage(away_wins, away_losses)
        if home_pct < away_pct:
            eastern_teams_home_lower_away.append(team['Team'])

print("(1) Eastern teams with home win-loss percentage lower than away:")
print(eastern_teams_home_lower_away)

# Question 2
eastern_pf_pa_diff = 0
western_pf_pa_diff = 0
eastern_teams_count = 0
western_teams_count = 0

for team in data:
    pf = int(team['PF'])
    pa = int(team['PA'])
    pf_pa_diff = pf - pa
    if team['Conference'] == 'Eastern':
        eastern_pf_pa_diff += pf_pa_diff
        eastern_teams_count += 1
    else:
        western_pf_pa_diff += pf_pa_diff
        western_teams_count += 1

eastern_avg_pf_pa_diff = eastern_pf_pa_diff / eastern_teams_count
western_avg_pf_pa_diff = western_pf_pa_diff / western_teams_count

print("\n(2) Conference with higher average PF-PA difference:")
if eastern_avg_pf_pa_diff > western_avg_pf_pa_diff:
    print("Eastern Conference")
else:
    print("Western Conference")

# Question 3
teams_ranked = sorted(data, key=lambda team: int(team['CONF']) / (int(team['CONF']) + int(team['DIV'])), reverse=True)

print("\n(3) Ranking list based on win percentage against the other conference:")
for rank, team in enumerate(teams_ranked, start=1):
    print(f"{rank}. {team['Team']}")