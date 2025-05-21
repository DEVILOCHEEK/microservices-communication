from flask import Flask
import requests

app = Flask(__name__)

@app.route("/call-service-b")
def call_service_b():
    response = requests.get("http://localhost:5001/data")
    return f"Service B said: {response.text}"

if __name__ == '__main__':
    app.run(port=5000)
