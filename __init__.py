import itertools
import random
import csv


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

def csv_export(pairs):
    tournament = "/home/egnyte/tournament.csv"
    with open(tournament, 'w', newline='') as tournament:
        wr = csv.writer(tournament, quoting=csv.QUOTE_ALL)
        wr.writerow(pairs)


# Teams input
# Generate csv with fixture
# Add manually results in csv file
# Import csv and generate table with points and choose winner