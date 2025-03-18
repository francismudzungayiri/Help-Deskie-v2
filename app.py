from flask import Flask
from controller import controllers



app = Flask(__name__)

@app.route('/')
def index():
    return controllers.appController.index()


@app.route('/login')
def login():
    return controllers.appController.login()


if __name__ == 'main':
    app.run(debug=True)