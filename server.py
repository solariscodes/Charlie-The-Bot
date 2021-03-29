from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hi! How are you?"

def run():
  app.run(host='0.0.0.0',port=80)
def keep_alive():
    t = Thread(target=run)
    t.start()
