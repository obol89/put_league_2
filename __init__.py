import itertools
import random


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
