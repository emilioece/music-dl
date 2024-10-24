from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "sup"})

@app.route('/api/search-track', methods=['POST'])
def submit_link():
    data = request.get_json()
    link = data.get('link')
    print(f"Received link: {link}")
    return jsonify({"message": f"Link received: {link}"})

if __name__ == '__main__':
    app.run(debug=True)
