import itertools
import random
import csv
import os.path
import pandas as pd
import string


#def get_teams():
#    teams = []
#    new_team = ''
#    while len(teams) != 16:
#        new_team = input("Please provide 16 names of teams that will \
#            participate in the tournament. \
#                Press eneter to confirm every name.")
#        teams.append(new_team)
#    print("You've provided 16 teams. Thank you.")
#    return teams


def get_team_pairs(teams):
    pairs = list(itertools.combinations(teams, 2))
    random.shuffle(pairs)
    return pairs


def get_team_groups(teams, n):
    n = 4
    random.shuffle(teams)
    for i in range(0, len(teams), n):
        val = teams[i:i+n]
        if len(val) == n:
            yield tuple(val)


def csv_export(teams):
    tournament_path = "~/tournament.csv"
    full_tournament_path = os.path.expanduser(tournament_path)
    # with open(tournament, 'w', newline='') as tournament:
    #    wr = csv.writer(tournament, quoting=csv.QUOTE_ALL)
    #    wr.writerow(pairs)
    with open(full_tournament_path, 'w') as tournament:
        wr = csv.writer(tournament)
        for line in teams:
            wr.writerow(line)


def csv_data(teams):
    columns = []
    number_of_groups = len(teams)
    for i in range(number_of_groups):
        columns.append('Group_' + list(string.ascii_uppercase)[i])
    data = pd.DataFrame(columns=columns)
    for group, column in zip(teams, data):
        data[column] = group
        
    return data

def get_data_structure(data):
    data.loc[-1] = data.columns 
    data.index = data.index + 1 
    data.sort_index(inplace=True) 
    data = pd.Series(data.values.ravel('F'))
    first_phase = ['','','','','','A1', 'B2','', 'B1', 'A2','', 'C1', 'D2','', 'D1', 'C2','','','','']
    second_phase = ['','','','','','','','','Semifinals','','','','Semifinals','','','','','','','']
    final = ['','','','','','','','','','','Final','','','','','','','','','']
    excel = pd.DataFrame({'Groups':data, '1/8':first_phase, '1/4':second_phase,  'final':final})

    return excel




