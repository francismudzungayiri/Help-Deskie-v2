from asyncio import tasks
from  flask import render_template, request, redirect, url_for, session
from controller import forms, standalone
from models import TaskModel, UserModel



class appController():
    

    @staticmethod
    def index():
        add_task_form = forms.addTaskForm()
        tk = TaskModel.Task_Model(username=None, role=None)  # or just TaskModel.Task_Model()

        if add_task_form.validate_on_submit():
            name = add_task_form.name.data
            office_number = add_task_form.office_number.data
            department = add_task_form.department.data
            challange = add_task_form.challange.data
            
            now = standalone.getFormattedDateNow()  
                       
            tk.insertData(fullname=name,office_number=office_number,
            department=department,challange=challange,date=now)
            
        return render_template('index.html', form = add_task_form)
    
    
    @staticmethod
    def login():        
        loginForm = forms.loginForm()
        user_id = None
        
        if request.method == 'POST':
            email = loginForm.username.data
            password = loginForm.password.data
            
            user = UserModel.User.get_user_email(email)
            if user:
                if user.verify_password(password):
                    session['email'] = user.get_email_address()
                    session['id'] = user.get_user_id()
                    session['first_name'] =user.get_firstname()
                    session['username'] = user.get_username()
                    session['role'] = user.get_role()
                    session['status'] = user.get_status()
                    
                    user_id = session.get('id')
            
            
            return redirect(url_for('dashboard', id = user_id ))
        return render_template('login.html', form = loginForm)
    
    @staticmethod
    def dashboard():
        #sessions variables
        firstname = session.get('first_name')
        email_sesseion = session.get('email')
        user_id = session.get('id')
        username = session.get('username')
        role = session.get('role')
        
        print(user_id)
        print(email_sesseion)
        print(firstname)
        print(username)
        print(role)

        #add team member form       
        member_form = forms.addTeamMember()
        if request.method == 'POST' and member_form.validate_on_submit():
            firstname = member_form.firstname.data
            lastname = member_form.lastname.data
            username = member_form.username.data
            email = member_form.email.data
            role = member_form.system_role.data
            password = member_form.password.data
            
            from app import bcrypt
            hashed_password = bcrypt.generate_password_hash(password)
            UserModel.User.add_team_member(firstname, lastname, username, email,  role, hashed_password)
        
        all_users = [user for user in UserModel.User.getAllUsers()]
        
        pending_tasks = TaskModel.Task_Model(username, role).get_all_pending_tasks()
# Removed unused variable completed_tasks_
        
        
        
        return render_template('dashboard.html', 
                               add_member_form = member_form,
                               users = all_users,
                               id = user_id,
                               email = email_sesseion,
                               firstname = firstname,
                               pending_tasks = pending_tasks,
                               )
    
    
    @staticmethod
    def task_details():
        
        id = session.get('id')
        task_id = request.args.get('id')
        task = TaskModel.Task_Model(username=None, role=None).get_task_by_id(task_id)
        return render_template('task_details.html', task = task)
    
    @staticmethod
    def logout():
        session.pop('email', None)
        session.pop('id', None)
        session.pop('first_name', None)
        session.pop('username', None)
        session.pop('role', None)
        session.pop('status', None)

        return redirect(url_for('login'))