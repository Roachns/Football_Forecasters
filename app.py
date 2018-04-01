from flask import Flask, jsonify, render_template
import pandas as pd

data = pd.read_csv('Data/team_logits.csv')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/logit/<team>/')
def get_logit(team):
    row = data.loc[data['TEAM'] == team].values[0]
    value = row[1]
    return jsonify(value)


@app.route('/teams/')
def team_list():
    teams = data['TEAM'].tolist()
    return jsonify(teams)


if __name__ == "__main__":
    app.run(debug=True)