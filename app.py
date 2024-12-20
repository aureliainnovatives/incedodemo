from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Advanced CI/CD Demo!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    return jsonify({"input": data, "output": "predicted-value"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

