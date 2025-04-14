from services.database import db

class Task_Model:
    
    def __init__(self, username, role):
        self.collection = db['querries']
        self.username = username
        self.role = role
        self.tasks = []
        
    
    # get all querries
    def get_all_pending_tasks(self):
        if self.role == "admin":
            self.tasks = list(db['querries'].find({"status": "pending"}))
            print(self.tasks)
        elif self.role == "user":
            self.tasks = list(db['querries'].find({"status": "pending", "username": self.username}))
        
        return self.tasks
        
        
    # get all querries
    def get_all_completed_tasks(self,):
        if self.role == "admin":
            self.tasks = db['querries'].find({"status": "completed"})
        elif self.role == "user":
            self.tasks = db['querries'].find({"status": "completed", "username": self.username})
        return self.tasks   
    
    #get all completed querries
    def get_all_completed_tasks(self):
        if self.role == "admin":
            self.tasks = list(db['querries'].find({"status": "completed"}))
        elif self.role == "user":
            self.tasks = list(db['querries'].find({"status": "completed", "username": self.username}))
        return self.tasks
    
    
    #get pending tasks by id
    def get_pending_task_by_id(self,id):
        self.tasks = db['querries'].find_one({"_id": id})
        return self.tasks

    #update a task status
    def update_task_status(self,id, status):
        self.tasks = db['querries'].update_one({"_id": id}, {"$set": {"status": status}})
        return self.tasks
    
    
    #insert one task into the DB
    def insertData(self, fullname, department, office_number, challange, date):
        data = {
            "fullname": fullname,
            "office_number": office_number,
            "department": department,
            "challange": challange,
            "date": date,
            "status": "pending",
        }
        self.collection.insert_one(data)
        
    
    
    #delete a certain task from the DB
    def delete_task(self, id):
        self.tasks = db['querries'].delete_one({"_id": id})
        return self.tasks
