from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    
    return jsonify({"message": "Hello aomezzzzzzzzzzzzzz"})

@app.route('/api/goodbye', methods=['GET'])
def goodbye():
    return jsonify({"message": "Goodbye from Flask API!"})

@app.route('/')
def home():
    return "<h1>Welcome to Noey's Flask API</h1><p>Try /api/hello or /api/goodbye</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)