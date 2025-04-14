from flask import Flask, url_for
from models.UserModel import User
from controller.controllers import appController
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager




app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

bcrypt = Bcrypt(app)


#settup flask login
login_manager = LoginManager()
login_manager.init_app(app)




controller = appController()

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/', methods=['POST', 'GET'])
def index():
    return controller.index()


@app.route('/login', methods=['POST','GET'])
def login():
    return controller.login()


@app.route('/dashboard/<id>', methods =['GET', 'POST'])
def  dashboard(id):
    return controller.dashboard()

@aapp.route('/dashboard/<id>/tasks/<task_id>', methods =['GET', 'POST'])
def task(id, task_id):
    return controller.task_details()


if __name__ == 'main':
    app.run(debug=True)