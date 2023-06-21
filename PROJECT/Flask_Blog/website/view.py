from flask import Blueprint, render_template, request, flash, jsonify,redirect,url_for
from flask_login import login_required, current_user
from .models import Note,User
from . import db

views = Blueprint('views', __name__)
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note') 
        if len(note) < 1:
            flash('Post is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id,name=current_user.name) 
            db.session.add(new_note) 
            db.session.commit()
            flash('Post added!', category='success')


    return render_template("home.html", user=current_user)


@views.route('/delete-note/<id>',methods=['POST','GET'])
@login_required
def delete_note(id):
    Notes = Note.query.filter_by(user_id=id).first()
    db.session.delete(Notes)
    db.session.commit()
    return redirect(url_for('views.home'))

@views.route('/post')
def posts():
    post = Note.query.all()
    return render_template('Posts.html', user=current_user, s=post)

