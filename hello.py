from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import backend
import ast
import json

app = Flask(__name__)


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
    # put_team = User(name = teams)
    # teams_db.session.add(put_team)
    # teams_db.session.commit()

    return jsonify(result={'status': 200})


@app.route('/a', methods=['GET'])
def team_sender():
    set_team = put_team.stack[0]
    put_team.reset()
    groups = [team for team in backend.get_team_groups(set_team, 4)]
    print(groups)

    # put_team = User(name = teams)
    # teams_db.session.add(put_team)
    # teams_db.session.commit()

    return render_template('index.html', data=set_team)


if __name__ == '__main__':
    app.run(debug=True)
