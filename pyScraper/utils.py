import pywhatkit
from datetime import datetime, timedelta

current_time = datetime.now()
new_time = current_time + timedelta(minutes=3)

def send_whatsapp_msg(phone: str, message: str):
    try:
        pywhatkit.sendwhatmsg(phone, message, new_time.hour, new_time.minute)
        return True
    except:
        return False