import time
import requests
from utils import load_messages, clear_messages

# Clear messages at 8:00 AM
def schedule_messages():
    while True:
        now = time.localtime()
        if now.tm_hour == 8 and now.tm_min == 0:
            clear_messages()
        time.sleep(60)

