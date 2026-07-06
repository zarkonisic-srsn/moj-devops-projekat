from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Zdravo iz DevOps svijeta!</h1><p>Ovo je moj prvi korak.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)