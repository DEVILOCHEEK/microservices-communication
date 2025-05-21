from flask import Flask

app = Flask(__name__)

@app.route("/data")
def get_data():
    return "Hello from Service B"

if __name__ == '__main__':
    app.run(port=5001)
