from flask import Blueprint, request, jsonify, render_template
from datetime import datetime, time, timedelta
from utils import load_messages, clear_messages, get_countdown

message_bp = Blueprint('message', __name__, url_prefix='/message')
submit_bp = Blueprint('submit', __name__, url_prefix='/submit')
index_bp = Blueprint('index', __name__)

# Handle incoming messages
@message_bp.route('', methods=['POST'])
def handle_message():
    # Check time of day
    now = datetime.now().time()
    if now < time(8, 0) or now > time(15, 0):
        return jsonify({'error': 'Messages can only be sent between 8:00 AM and 3:00 PM', 'countdown': get_countdown()}), 400

    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Request body is empty'}), 400
    message = data.get('message')
    if message is None:
        return jsonify({'error': 'Missing "message" field'}), 400
    print(f'Received message: {message}')

    # Write to JSON file
    data = {
        "time": datetime.now().strftime("%m/%d/%Y %H:%M:%S"),
        "message": message
    }
    with open("CPCCOMMS.json", "a") as f:
        json.dump(data, f)
        f.write("\n")

    # Add message to list
    messages.append(data)

    # Echo back message
    return jsonify({'message': f'You said: {message}'})

# Render form page
@index_bp.route('/', methods=['GET'])
def index():
    theme = 'light' if time(8, 0) <= datetime.now().time() <= time(15, 0) else 'dark'
    return render_template('form.html', theme=theme)

# Handle form submission
@submit_bp.route('', methods=['POST'])
def submit():
    # Check time of day
    now = datetime.now().time()
    if now < time(8, 0) or now > time(15, 0):
        return render_template('error.html', message='Messages can only be sent between 8:00 AM and 3:00 PM',
                               countdown=get_countdown())

    message = request.form['message']

    # Send message to server
    response = requests.post('http://localhost:8080/message', json={'message': message})

    # Return response
    return render_template('response.html', message=message, response=response.json()['message'], messages=messages)


