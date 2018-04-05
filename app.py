from flask import Flask, jsonify, render_template, request
import pandas as pd
import math
import json

data = pd.read_csv('Data/2017_team_data.csv')


#--------------------------------
#APP FUNCTIONS
#--------------------------------

def team_search(team_a, team_b):
    row_a = data['TEAM'] == team_a
    row_b = data['TEAM'] == team_b

    result_a = data[row_a].values[0].tolist()
    result_b = data[row_b].values[0].tolist()

    results = {
        'A':result_a,
        'B':result_b
    }

    return results


def probability(logit_team_a, logit_team_b):

    logit_game = -0.03 + 0.13 + logit_team_a - logit_team_b
    odds = math.exp(logit_game)
    prob_a = odds/(1+odds)
    prob_b = 1-prob_a

    results = [prob_a, prob_b]

    return results


#--------------------------------
#FLASK ROUTES
#--------------------------------

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def project_about():
    return render_template('about.html')


@app.route('/team/')
def project_team():
    return render_template('team.html')


@app.route('/teams/')
def get_teams():
    teams = [{'TEAM':'default', 'NAME':'Choose Team'}]

    for index, row in data.iterrows():
        team = row['TEAM']
        name = row['NAME']
        teams.append({'TEAM':team, 'NAME':name})
    
    return jsonify(teams)


@app.route('/game/')
def get_game():
    a = request.args.get('a')
    b = request.args.get('b')

    team_data = team_search(a, b)
    game_prob = probability(team_data['A'][2], team_data['B'][2])

    results = [
        {
            'Win probability': game_prob[0],
            'Team': team_data['A'][1],
            'Abbr': team_data['A'][0],
            'OPASS': round(team_data['A'][3], 2),
            'ORUSH': round(team_data['A'][4], 2),
            'OINT': round(team_data['A'][5], 2),
            'DPASS': round(team_data['A'][6], 2),
            'DRUSH': round(team_data['A'][7], 2),
            'TPEN': round(team_data['A'][8], 2)
        },
        {
            'Win probability': game_prob[1],
            'Team': team_data['B'][1],
            'Abbr': team_data['B'][0],
            'OPASS': round(team_data['B'][3], 2),
            'ORUSH': round(team_data['B'][4], 2),
            'OINT': round(team_data['B'][5], 2),
            'DPASS': round(team_data['B'][6], 2),
            'DRUSH': round(team_data['B'][7], 2),
            'TPEN': round(team_data['B'][8], 2)
        }
    ]

    #return jsonify(results)
    return json.dumps(results)


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)