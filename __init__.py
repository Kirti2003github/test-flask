from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
app=Flask(__name__)


app.config['SECRET_KEY']='07a31d60d642e219187ce84d7e02ae3f7eab461ac1c755868b98a5c390084794'

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

#from main.forms import RegisterationForm, LoginForm,UpdateAccountForm
from main import routes