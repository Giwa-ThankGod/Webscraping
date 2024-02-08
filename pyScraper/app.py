from flask import Flask, render_template, request, redirect, url_for

import sys
sys.path.append('C:\Webscraping\pyScraper')
from index import free_super_tips, mrfixitstips, mighty_tips, thehardtackle, scores_24

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/prediction', methods=['POST'])
def prediction():
    if request.method == 'POST':
        team1 = request.form['team1']
        team2 = request.form['team2']

        predictions = []

        a = free_super_tips(team1, team2)
        b = mighty_tips(team1, team2)
        c = mrfixitstips(team1, team2)
        d = scores_24(team1, team2)
        e = thehardtackle(team1, team2)

        predictions.append(a)
        predictions.append(b)
        predictions.append(c) 
        predictions.append(d) 
        predictions.append(e)

        data = {
            'team1': team1,
            'team2': team2,
            'predictions': predictions
        }
    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)