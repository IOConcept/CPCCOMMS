from datetime import datetime, time, timedelta

def get_countdown():
    now = datetime.now()
    if now.time() < time(8, 0):
        # Before 8:00 AM
        target_time = datetime.combine(now.date(), time(8, 0))
    else:
        # After 3:00 PM
        target_time = datetime.combine(now.date() + timedelta(days=1), time(8, 0))
    time_left = target_time - now
    return str(time_left)

def load_messages():
    messages = []
    with open('CPCCOMMS.json') as f:
        for line in f:
            data = json.loads(line.strip())
            messages.append(data)
    return messages

def clear_messages():
    with open('CPCCOMMS.json', 'w') as f:
        pass
