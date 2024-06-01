from flask import Flask

app = Flask(__name__)

@app.route("/")
def prints():
    return "Hi!"

