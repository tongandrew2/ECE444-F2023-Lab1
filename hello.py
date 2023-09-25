from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'lab1test'

class NameForm(FlaskForm):
 name = StringField("What is your name?", validators=[DataRequired()])
 email = StringField("What is your UofT Email address?", validators=[Email()])
 submit = SubmitField('Submit')
@app.route('/', methods=['GET', 'POST'])
def index():
 name = None
 email = None
 uoft_email = False
 form = NameForm()
 if form.validate_on_submit():
  old_name = session.get('name')
  if old_name is not None and old_name != form.name.data:
   flash("Name has been changed.")
  old_email = session.get('email')
  if old_email is not None and old_email != form.email.data:
   flash("Email has been changed.")

  if 'utoronto' in form.email.data:
   uoft_email = True
  else:
   uoft_email = False

  session['name'] = form.name.data
  session['email'] = form.email.data
  session['uoft_email'] = uoft_email
  
  return redirect(url_for('index'))
 return render_template('index.html', form=form, name=session.get('name'), email = session.get('email'), uoft_email = session.get("uoft_email"))

@app.route('/user/<name>/')
def user(name):
 return render_template('user.html', name=name, current_time=datetime.utcnow())
