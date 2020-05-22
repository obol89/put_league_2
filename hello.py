from flask import Flask, request, render_template, jsonify, Response
import pandas as pd
import backend
import ast

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


class Storage(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def reset(self):
        self.stack = []


put_team = Storage()


@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    teams = request.form.getlist('teams')
    teams = teams[0]
    teams = ast.literal_eval(teams)
    teams.pop(0)
    put_team.push(teams)

    return jsonify(result={'status': 200})


@app.route('/teams')
def team_sender():
    set_team = put_team.stack[0]
    put_team.reset()
    groups = [team for team in backend.get_team_groups(set_team, 4)]
    put_team.push(groups)

    return render_template('teams.html', groups=groups)

@app.route('/end')
def get_csv():
    return render_template('end.html')

@app.route('/summary')
def get_structure():
    csv_groups = put_team.stack[0]
    put_team.reset()
    excel = backend.csv_data(csv_groups)
    excel = backend.get_data_structure(excel)

    return Response(excel.to_csv(index=False, header=False), 
    mimetype="text/csv", headers={"Content-disposition": "attachment; filename=PUT-table_group.csv"})


if __name__ == '__main__':
    app.run(debug=True)
