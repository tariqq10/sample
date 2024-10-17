from flask import Flask, jsonify

app = Flask(__name__)

# Simple route to return a JSON response
@app.route('/')
def home():
    return jsonify(message="Welcome to your Flask API! It's working."), 200

@app.route('/api/data')
def get_data():
    data = {
        "name": "Flask API",
        "version": "1.0",
        "description": "A simple API for deployment testing on Render."
    }
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
