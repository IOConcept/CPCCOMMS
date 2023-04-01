from flask import Flask, jsonify, render_template, request
from routes import message_bp, submit_bp, index_bp
from scheduler import schedule_messages
from threading import Thread
import schedule
import time

app = Flask(__name__)

# Clear messages at 8:00 AM
schedule.every().day.at("08:00").do(schedule_messages)

# Register routes
app.register_blueprint(message_bp, url_prefix='/message')
app.register_blueprint(submit_bp, url_prefix='/submit')
app.register_blueprint(index_bp)


def run_background_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    # Start background scheduler thread
    scheduler_thread = Thread(target=run_background_scheduler)
    scheduler_thread.start()

    app.run(host='0.0.0.0', port=8080)
