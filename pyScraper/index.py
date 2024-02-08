import requests
from bs4 import BeautifulSoup
from datetime import date as DATE

# Import for scraping dynamic web pages
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

team1 = 'South Africa'
team2 = 'Tunisia'

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
            return {"title": "freesupertips", "predictions": None}

        game_date = soup.find(class_="GameBullets").find_all("li")[0:2]
        game_date = [i.text for i in game_date ] # [19:00, Today]

        prediciton_tag = soup.find_all(class_="IndividualTipPrediction")
        predicitons = []
        for prediciton in prediciton_tag:
            predicitons.append(prediciton.find("h4").text) # ['Over 2.5 Match Goals', 'AFC Bournemouth 3-1', 'Dominic Solanke To Score Anytime']

        return {"title": "freesupertips", "predictions": predicitons}
    except Exception as error:
        return {"title": "freesupertips", "predictions": None}

def mighty_tips(team1: str, team2: str):
    team1 = team1.lower().split(' ')[0]
    team2 = team2.lower().split(' ')[0]
    date = DATE.today().strftime('%d-%m-%Y')

    URL = f"https://www.mightytips.com/football-predictions/{team1}-vs-{team2}-prediction-{date}/"
    try:
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        page_not_found = soup.find(class_="mtl-page404")
        if page_not_found:
            return {"title": "mightytips", "predictions": None}
        
        # prediction = soup.find(class_="mtl-content-block-margin mtl-content-style mtl-clearfix").find_all("h2")[1]
        # prediction = prediction.text.split(":")[1]

        predictions = []
        prediction = soup.find(class_="mtl-prediction-main2__name")
        predictions.append(prediction.text)
        return {"title": "mightytips", "predictions": predictions}
    except Exception as error:
        return {"title": "mightytips", "predictions": None}
    
def scores_24(team1: str, team2: str):
    team1 = team1.lower().replace(' ', '-')
    team2 = team2.lower().replace(' ', '-')
    date = DATE.today().strftime('%d-%m-%Y')

    URL = f"https://scores24.live/en/soccer/m-{date}-{team1}-{team2}-prediction"
    try:
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        page_not_found = soup.find(class_="sc-12l8pnt-1")
        if page_not_found:
            return {"title": "scores24", "predictions": None}
    
        prediction = soup.find(class_="sc-10cwpmp-2")
        prediction_odd = soup.find(class_="sc-10cwpmp-3")
        return {"title": "scores24", "predictions": [prediction.text, prediction_odd.text]}
    except Exception as error:
        return {"title": "scores24", "predictions": None}
    
def mrfixitstips(team1: str, team2: str):
    team1 = team1.lower().replace(' ', '-')
    team2 = team2.lower().replace(' ', '-')

    URL = f"https://mrfixitstips.co.uk/previews/{team1}-vs-{team2}-prediction-and-betting-tips/"

    try:
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        try:
            page_not_found = soup.find(class_="page-title")
            if "404" in page_not_found.text.lower():
                return {"title": "mrfixitstips", "predictions": None}
        except:
            pass
    
        predictions_tag = soup.find_all(class_="row alt_colors")
        predictions = []
        for prediction in predictions_tag:
            predictions.append(prediction.find(class_="col-md-6").find("strong").text)
        
        return {"title": "mrfixitstips", "predictions": predictions}
    except Exception as error:
        return {"title": "mrfixitstips", "predictions": None}

def football_whispers(team1: str, team2: str):
    team1 = team1.lower().replace(' ', '-')
    team2 = team2.lower().replace(' ', '-')

    URL = f"https://footballwhispers.com/blog/{team1}-vs-{team2}-prediction/"

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)

    # Create a Chrome webdriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)

    # Wait for the page to load (you may need to adjust the waiting time)
    driver.implicitly_wait(5)

    # Extract the content after JavaScript execution
    dynamic_content = driver.page_source

    try:
        soup = BeautifulSoup(dynamic_content, "html.parser")

        try:
            page_not_found = soup.find(class_="football-container-header-single").find("h1")
            if page_not_found.text.lower() == "not found":
                print(False)
                return {"title": "footballwhispers", "predictions": None}
        except:
            pass
    
        prediction1 = soup.find(class_="tip_tip")
        # prediction2 = soup.find(class_="sc-10cwpmp-3")
        print(prediction1)
    except Exception as error:
        print('[Error]: ', error)
        return {"title": "footballwhispers", "predictions": None}
    
# football_whispers(team1, team2)
    
def thehardtackle(team1: str, team2: str) -> dict:
    team1 = team1.lower().replace(' ', '-')
    team2 = team2.lower().replace(' ', '-')
    date = DATE.today().strftime('%Y/%m/%d')

    URL = f"https://thehardtackle.com/round-up/{date}/{team1}-vs-{team2}-preview-and-prediction/"

    try:
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        try:
            page_not_found = soup.find(class_="jeg_archive_title")
            if page_not_found.text.lower() == 'page not found':
                return {"title": "thehardtackle", "predictions": None}
        except:
            pass
    
        predictions_tag = soup.find(class_="content-inner").find_all("h4")[-1]
        return {"title": "thehardtackle", "predictions": [predictions_tag.text]}
    except Exception as error:
        return {"title": "thehardtackle", "predictions": None}

