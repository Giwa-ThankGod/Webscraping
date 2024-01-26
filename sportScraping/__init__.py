from utils import send_whatsapp_msg
from index import free_super_tips, mrfixitstips, mighty_tips, thehardtackle, scores_24

def predictions(team1, team2):
    a = free_super_tips(team1, team2)
    b = mighty_tips(team1, team2)
    c = mrfixitstips(team1, team2)
    d = scores_24(team1, team2)
    e = thehardtackle(team1, team2)

    message = f"""
    PREDICTIONS:
    Teams: {team1} vs {team2}\n
    freesupertips: {a},\n
    migthytips: {b},\n
    mrfixitstips: {c},\n
    scores24: {d},\n
    thehardtackle: {e}
    """

    send_whatsapp_msg("+2348055287181", message)

if __name__ == "__main__":
    predictions("Bournemouth","Swansea")