import requests
from bs4 import BeautifulSoup

team1 = 'Qatar'
team2 = 'China'

def free_super_tips(team1, team2):
    team1 = team1.lower().replace(' ', '-')
    team2 = team2.lower().replace(' ', '-')
    URL = f"https://www.freesupertips.com/predictions/{team1}-vs-{team2}-predictions-betting-tips-match-previews/"

    try:
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        game_date = soup.find(class_="GameBullets").find_all("li")[0:2]
        game_date = [i.text for i in game_date ] # [19:00, Today]
        print(game_date)

        game_prediciton = soup.find(class_="IndividualTipPrediction")
        game_prediciton = game_prediciton.find_all("h4") # [ Both Teams to Score ]

        print(game_prediciton[0].text)
    except Exception as error:
        print('Something went wrong!!!')
        print(f'[ERROR]: {error}')




free_super_tips(team1, team2)

