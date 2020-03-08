from app import app
from flask import render_template
from app.form import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'fuckboi'}
    return render_template('booking.html', title='LMAO', user=user)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)