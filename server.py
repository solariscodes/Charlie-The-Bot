from flask import Flask
from threading import Thread

porta = int(os.environ.get('PORT', 5000))

app = Flask('')

@app.route('/')
def home():
    return "Hi! How are you?"

def run():
  app.run(host='0.0.0.0',port=porta)
def keep_alive():
    t = Thread(target=run)
    t.start()
