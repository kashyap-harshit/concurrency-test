from flask import Flask
import time

app = Flask(__name__)


@app.route("/")
def home():
    time.sleep(5)
    return "WSGI response after 5 seconds"

