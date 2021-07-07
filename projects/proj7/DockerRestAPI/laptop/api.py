# Laptop Service

import os
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, session
from flask_restful import Resource, Api, request, reqparse
from pymongo import MongoClient
from wtforms import Form, BooleanField, StringField, PasswordField,validators,SubmitField
from wtforms.validators import DataRequired
from password import hash_password, verify_password
from flask_login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin,
                            confirm_login, fresh_login_required)
from testToken import generate_auth_token, verify_auth_token
from flask_wtf import FlaskForm

# Instantiate the app
app = Flask(__name__)
api = Api(app)
SECRET_KEY = "The last Project"
app.config['SECRET_KEY'] = SECRET_KEY

DEBUG = True

client = MongoClient("dockerrestapi_db_1", 27017)
#client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.tododb
db2 = client.user

id = 0

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Sign up')
    
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/jump')
def jump():
    return render_template("jump.html")

@app.route('/user_existed')
def user_existed():
    return render_template("user_existed.html"),400

@app.route('/user_not_found')
def user_not_found():
    return render_template("user_not_found.html"),400

@app.route('/logout')
def out():
    return render_template("logout.html")
    
@app.route('/login', methods = ["GET", "POST"])
def login():
    global id
    form = LoginForm()
    app.logger.debug("form.validate_on_submit = {}".format(form.validate_on_submit()))
    if form.validate_on_submit():
        username = form.username.data
        useresult = db2.user.find_one({"user":username})
        password = form.password.data
        remember_me = form.remember_me.data
        app.logger.debug("remember_me = {}".format(remember_me))
        if useresult == None:
            return render_template('user_not_found.html')
        else:
            if verify_password(password, useresult["password"]):
            
                generate_auth_token(id,600)
                return redirect(url_for('jump'))
    return render_template('login.html',form = form)
    
@app.route('/register',methods = ["GET","POST"])
def register():
    global id
    form = RegisterForm()
    app.logger.debug("form.validate_on_submit = {}".format(form.validate_on_submit()))
    if form.validate_on_submit():
        username = form.username.data
        app.logger.debug("username={}".format(username))
        password = hash_password(form.password.data)
        userresult = db2.user.find_one({"user":username})
        if userresult != None:
            return render_template('user_existed.html')
        else:
            db2.user.insert({"id": id, "user":username,"password":password})
            id += 1
            return redirect(url_for('index'))
    return render_template('register.html',form=form)
    
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))
@app.route("/token")

class Laptop(Resource):
    def get(self):
        return {
            'Laptops': ['Mac OS', 'Dell', 
            'Windozzee',
	    'Yet another laptop!',
	    'Yet yet another laptop!'
            ]
        }
        
#List all
class ListAll(Resource):
    def get(self):
        _items = db.tododb.find()
        items = [item for item in _items]
        opentime = [item["open"] for item in items]
        closetime = [item["close"] for item in items]
        return {'Opentime':opentime, 'Closetime': closetime}
    
#List all, opentime only
class ListOpenAll(Resource):
    def get(self):
        _items = db.tododb.find()
        items = [item for item in _items]
        opentime = [item["open"] for item in items]
        return {'Opentime': opentime}
    
#List all, closetime only
class ListCloseAll(Resource):
    def get(self):
        _items = db.tododb.find()
        items = [item for item in _items]
        closetime = [item["close"] for item in items]
        return {'Closetime': closetime}
    
#List all
#use csv or json
class Timeallformat(Resource):
    def get(self,format):
        _items = db.tododb.find()
    
        if format == 'csv':
            items = [item for item in _items]
            opentime = [item["open"] for item in items]
            closetime = [item["close"] for item in items]
            open_csv = ""
            close_csv = ""
            for b in opentime:
                open_csv += b + ', '
            for a in closetime:
                close_csv += a + ', '
            return 'Opentime: '+ open_csv + ' Closetime: ' + close_csv
    
        elif format == 'json':
            items = [item for item in _items]
            opentime = [item["open"] for item in items]
            closetime = [item["close"] for item in items]
            return {'Opentime':opentime, 'Closetime': closetime}
        
#List all, opentime only
#use csv or json
class Openallformat(Resource):
    def get(self, format):
        _items = db.tododb.find()
    
        n = request.args.get('top', type = int)
        items = [item for item in _items]
    
        if  format == 'csv' :
            opentime = [item["open"] for item in items]
            if n != None:
                if n > len(items):
                    n = len(items)
                open = ""
                for i in range(n):
                    open += opentime[i] + ', '
                return open
            else:
                open = ""
                for s in opentime:
                    open += s + ', '
                return open
    
        elif format == 'json':
            if n != None:
                if n > len(items):
                    n = len(items)
                opentime = []
                for i in range(n):
                    opentime.append(items[i]['open'])
                return {'opentime': opentime}

            else:
                opentime = [item["open"] for item in items]
                return {'Opentime': opentime}
            
#List all, closetime only
#use csv or json
class Closeallformat(Resource):
    def get(self,format):
        _items = db.tododb.find()
        
        n = request.args.get('top', type = int)
        items = [item for item in _items]
    
    
        if format == 'csv':
            closetime = [item["close"] for item in items]
            if n != None:
                if n > len(items):
                    n = len(items)
                close = ""
                for i in range(n):
                    close += closetime[i]  + ', '
                return close
            else:
                close = ""
                for s in closetime:
                    close += s + ', '
                return close

        elif format == 'json':
            if n != None:
                if n > len(items):
                    n = len(items)
                closetime = []
                for i in range(n):
                    closetime.append(items[i]['close'])
                return {'Closetime': closetime}
        
            else:
                closetime = [item["close"] for item in items]
                return {'Closetime': closetime}

# Create routes
# Another way, without decorators
api.add_resource(Laptop, '/')
api.add_resource(ListAll,'/listAll')

api.add_resource(ListOpenAll,'/listOpenOnly')
api.add_resource(ListCloseAll,'/listCloseOnly')

api.add_resource(Timeallformat,'/listAll/<format>')
api.add_resource(Openallformat,'/listOpenOnly/<format>')
api.add_resource(Closeallformat,'/listCloseOnly/<format>')



# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
