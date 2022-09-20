from flask import Flask, render_template
import random
import signal
import sys

def exit_gracefully(signumber, frame):
  print("Received signal", signumber, "cleaning up...")
  sys.exit(0)

app = Flask(__name__)

# list of cat images
images = [
    "https://placekitten.com/200/300",
    "https://placekitten.com/200/301",
    "https://placekitten.com/200/302",
    "https://placekitten.com/200/303",
    "https://placekitten.com/200/304",
    "https://placekitten.com/200/305",
    "https://placekitten.com/200/306",
    "https://placekitten.com/200/307",
    "https://placekitten.com/200/308",
    "https://placekitten.com/200/309"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, exit_gracefully)
    app.run(host="0.0.0.0",threaded=True)
