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
    data = data.tolist()
    df2 = [x for y in (data[i:i+5] + [''] * (i < len(data) - 2) for i in range(0, len(data), 5)) for x in y]
    df2.pop()
    A = ['Group stage', '']
    A.extend(df2)
    csv = {'Group stage': A,
            'break': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            'Quarterfinals': ['', 'Quarterfinals', '', 'A1', 'B2', '', '', '', '', 'B1', 'A2', '', '', '', '', 'C1', 'D2', '', '', '', '', 'D1', 'C2', '', ''],
            'Semifinals': ['', '', '', 'Semifinals', '', '', 'A1/B2', 'B1/A2', '', '', '', '', '', '', '', '', '', '', 'C1/D2', 'D1/C2', '', '', '', '', ''],
            'Final': ['', '', '', '', '', 'Final', '', '', '', '', '', '', 'A1/B2 - B1/A2', 'C1/D2 - D1/C2', '', '', '', '', '', '', '', '', '', '', ''],
    }
    excel = pd.DataFrame(csv, columns=['Group stage', 'break', 'Quarterfinals', 'break', 'Semifinals', 'break', 'Final'])
    return excel
