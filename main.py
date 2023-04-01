from flask import Flask
import schedule
from routes import message_bp, submit_bp, index_bp
from scheduler import schedule_messages
import time

app = Flask(__name__)

# Clear messages at 8:00 AM
schedule.every().day.at("08:00").do(schedule_messages)

# Register routes
app.register_blueprint(message_bp)
app.register_blueprint(submit_bp)
app.register_blueprint(index_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
