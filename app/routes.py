from app import app
from flask import render_template, abort, request, redirect, make_response
from flask_sqlalchemy import SQLAlchemy
import os
from random import choices
from string import ascii_letters, digits
from datetime import date
from calendar import Calendar



login_sessions = {}
cookee_length = 16

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, "calander.db")
app.secret_key = "correcthorsebatterystaple"
db.init_app(app)

import app.models as models
from app.form import Add_User, Add_date, changedate


 #   def getdate(year, month, day):
  #  today = date.today()
  #  print(today)
    #if dates.year < year:
    #    return True
    #elif dates.month < month:
    #    return True
    #elif dates.day < day:
    #    return True
    #else:
    #    return False    



@app.route("/")
def home():
    # result = models.Pizza.query.all()
    return render_template("home.html", is_loggedin=checklogin(request.cookies.get("login_cookie")))


@app.route('/about')
def about():
    return render_template("about.html", is_loggedin=checklogin(request.cookies.get("login_cookie")))


# @app.route('/add_movie', methods=['GET', 'POST'])
# def add_movie():
# form = Add_Movie()
# if request.method=='GET':
# return render_template('add_movie.html', form=form, title="Add A Movie")


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        acc = models.user.query.filter_by(name=str(username), password=str(password)).first()
        print(str(acc) == str(password), str(acc), str(password))
        if str(acc) == str(password):
            msg = 'Logged in successfully !'
            cookie = cookee()
            login_sessions.update({cookie: acc.id})
            resp = make_response(render_template('index.html', msg=msg, is_loggedin=checklogin(request.cookies.get("login_cookie"))))
            resp.set_cookie('login_cookie', cookie)
            return resp
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg=msg, is_loggedin=checklogin(request.cookies.get("login_cookie")))

def cookee():
    cookee = choices(ascii_letters + digits, k=cookee_length)
    while str(cookee) in login_sessions:
        cookee = choices(ascii_letters + digits, k=cookee_length)
    return str("".join(cookee))

def getdate(year, month, day):
    today = date.today
    if year > today.year:
        return False
    elif year > today.year:
        return True
    elif month > today.month:
        return False

    
    

@app.route('/calendar', methods=['GET', 'POST'])
def calendar():
    form = Add_date()
    month = changedate()
    year = month.year.data
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print(month.month.data)
    try:
        selectedmonth = month.month.data
        days = Calendar().monthdayscalendar(int(year), int(month.month.data) + 1)
    except Exception:
        selectedmonth = 1
        days = Calendar().monthdayscalendar(2024, 1)
    return render_template("add_date.html", form=form, is_loggedin=checklogin(request.cookies.get("login_cookie")), days=days, month=month, selectedmonth=months[int(selectedmonth)])

@app.route('/add_calendar', methods=["GET", "POST"])
def add_calendar():
    form = Add_date()
    if getdate(form.date.data.year, form.date.data.month, form.date.data.day):
        print("works")
        new_date = models.date()
        new_date.year = form.date.data.year
        new_date.month = form.date.data.month
        new_date.day = form.date.data.day
        new_date.message = form.message.data
        db.session.add(new_date)
        db.session.commit()
        return redirect("/")


def checklogin(cookie):
    if login_sessions.get(cookie) is not None:
        return True
    else:
        return False
    


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Add_User()
    users = models.user.query.filter_by(name=form.username.data).first()
    print(users)
    if request.method == "GET":
        return render_template("signup.html", form=form, invalid=False, is_loggedin=checklogin(request.cookies.get("login_cookie")))

    else:
        if users == None:
            new_user = models.user()
            new_user.name = form.username.data
            new_user.password = form.password.data
            db.session.add(new_user)
            db.session.commit()
            return redirect("/")    
        
        else:
            return render_template("signup.html", form=form, invalid=True, is_loggedin=checklogin(request.cookies.get("login_cookie")))
    pass


@app.route('/date')
def date():
    return render_template("date.html", is_loggedin=checklogin(request.cookies.get("login_cookie")))


# @app.route('/pizza/<int:id>')
# def Pizza(id):
# pizza = models.Pizza.query.filter_by(id=id).first()
# return render_template('pizza.html', pizza=pizza)

# @app.route('/add_pizza', methods=["GET", "POST"])
# def add_pizza():
# form = add_pizza()
# if request.method == "GET":
# new_pizza = models.Pizza()
# new_pizza.base.choices = [models.Base.query_all()]
# return render_template("add_pizza.html", form=form)
# else:
# if form.validate_on_submit():
# new_pizza = models.Pizza()
# new_pizza.name = form.name.data
# new_pizza.description = form.description.data
# new_pizza.base = form.description.data
# db.session.add(new_pizza)
# db.session.commit
# return redirect(url_for('pizza', id=new_pizza.id))
# else:
# return render_template('add_pizza.html', form=form)
# pass
