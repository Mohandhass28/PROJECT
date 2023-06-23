from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('Name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        Email = User.query.filter_by(email=email).first()
        User_name = User.query.filter_by(name=name).first()
        if Email:
            flash('Gmail is already in use. ', category='error')
        elif User_name:
            flash('User_Name is already in use. ', category='error')
        elif password1 != password2:
            flash('password don`t match!',category='error')
        elif len(name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters.', category='error')
        else:
            New_User = User(email=email,name=name,password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(New_User)
            db.session.commit()
            flash('Successfuly Created New Account')
            return redirect(url_for('views.home'))

    return render_template('sign_in.html',user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))