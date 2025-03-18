from  flask import render_template




class appController():
    
    @staticmethod
    def index():
        return render_template('index.html')
    
    
    @staticmethod
    def login():
        return render_template('login.html')