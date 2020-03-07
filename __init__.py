import itertools
import random
import csv
import os.path


def get_teams():
    teams = []
    new_team = ''
    while new_team != 'quit':
        new_team = input("Please provide name of team that will participate in the tournament. If you have provided all teams please enter 'quit': ")
        if new_team != 'quit':
            teams.append(new_team)
    return teams

def get_team_pairs(teams):
    pairs = list(itertools.combinations(teams, 2))
    random.shuffle(pairs)
    return pairs

def csv_export(teams):
    tournament_path = "~/tournament.csv"
    full_tournament_path = os.path.expanduser(tournament_path)
    #with open(tournament, 'w', newline='') as tournament:
    #    wr = csv.writer(tournament, quoting=csv.QUOTE_ALL)
    #    wr.writerow(pairs)
    with open(full_tournament_path, 'w') as tournament:
        wr = csv.writer(tournament)
        for line in teams:
            wr.writerow(line)


# Teams input
# Generate csv with fixture
# Add manually results in csv file
# Import csv and generate table with points and choose winner