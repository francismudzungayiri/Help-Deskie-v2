from pymongo import MongoClient 
from services.database import db 
from bson.objectid import ObjectId


class User():
    
    def __init__(self, user_data):
        self.id = str(user_data['_id'])
        self.email = user_data['email']
        self.password =  user_data['password']
        self.fistname = user_data['first_name']
        self.lastname = user_data['last_name']
        self.role = user_data['system_role']
        self.position = user_data['position']
        self.username = user_data['username']
        self.status = user_data['status']
        
    
    
    
    #get a user by email
    @staticmethod
    def get_user_email(email):
        user_data = db.users.find_one({'email': email})
        return User(user_data) if user_data else None
    
    
    @staticmethod 
    def get_user_by_id(user_id):
        user_data = db.users.find_one({"_id": ObjectId(user_id)})
        return User(user_data) if user_data else None
    
    #verify password
    def verify_password(self, password):
        from app import bcrypt
        return bcrypt.check_password_hash(self.password, password)
        
    
    @staticmethod
    def add_team_member(firstname, lastname, username, email,  role, password):
        data = {
                'first_name':firstname,
                'last_name': lastname,
                'username': username,
                'email': email,
                'system_role': role,
                'status':'Available',
                'password':password
            }
        db.users.insert_one(data)
        
        
    #get all users
    @staticmethod
    def getAllUsers():
        all_users = db.users.find()
        return all_users
    
    
    #GETTERS WHICH WE USE GET ATTRIBUTES VALUES
    
    #get user_ID
    def get_user_id(self):
        return self.id
    
    #get email address
    def get_email_address(self):
        return self.email
    
    #get username
    def get_username(self):
        return self.username
    
    #get firstname
    def get_firstname(self):
        return self.fistname
    
    
    #get lastname
    def get_lastname(self):
        return self.lastname
    
    #get your system role
    def get_role(self):
        return self.role
    
    
    #get system status
    def get_status(self):
        return self.status
    
    
    #get position
    def get_postion(self):
        return self.position
    