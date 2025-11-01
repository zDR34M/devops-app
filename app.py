from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Tareq's DevOps App 🚀</h1>"

@app.route('/status')
def status():
    return jsonify({"status": "running", "message": "App is healthy ✅"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
