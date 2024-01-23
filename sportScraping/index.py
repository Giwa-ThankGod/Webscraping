import requests
from bs4 import BeautifulSoup
from datetime import date as DATE

team1 = 'Mauritania'
team2 = 'Algeria'

def free_super_tips(team1: str, team2: str): 
    team1 = team1.lower().replace(' ', '-')
    team2 = team2.lower().replace(' ', '-')
    URL = f"https://www.freesupertips.com/predictions/{team1}-vs-{team2}-predictions-betting-tips-match-previews/"

    try:
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        # Checks if the page exist on the website.
        page_not_found = soup.find(class_="Main").find_all("h1")[0]
        if page_not_found.text == "404":
            print(False)
            return False

        game_date = soup.find(class_="GameBullets").find_all("li")[0:2]
        game_date = [i.text for i in game_date ] # [19:00, Today]
        # print(game_date)

        prediciton = soup.find(class_="IndividualTipPrediction")
        prediciton = prediciton.find_all("h4") # [ Both Teams to Score ]

        print(prediciton[0].text)
        # return prediciton
    except Exception as error:
        print('Something went wrong!!!')
        print(f'[ERROR]: {error}')
        return None




# free_super_tips(team1, team2)


def mighty_tips(team1: str, team2: str):
    team1 = team1.lower().split(' ')[0]
    team1 = team1.lower().split(' ')[0]
    date = DATE.today().strftime('%d-%m-%Y')
    # print(date)

    URL = f"https://www.mightytips.com/football-predictions/{team1}-vs-{team2}-prediction-{date}/"
    try:
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        page_not_found = soup.find(class_="mtl-page404")
        if page_not_found:
            print(False)
            return False
        
        # prediction = soup.find(class_="mtl-content-block-margin mtl-content-style mtl-clearfix").find_all("h2")[1]
        # prediction = prediction.text.split(":")[1]

        prediction = soup.find(class_="mtl-prediction-main2__name")
        print(prediction.text)
        return prediction.text
    except Exception as error:
        print('[Error]: ', error)
        return None

mighty_tips(team1, team2)