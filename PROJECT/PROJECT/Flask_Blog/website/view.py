from flask import Blueprint, render_template, request, flash,redirect,url_for
from flask_login import login_required, current_user
from .models import Note,User,images
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')
        if len(note) < 1:
            flash('Post is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id,name=current_user.name,like=0)
            db.session.add(new_note) 
            db.session.commit()
            flash('Post added!', category='success')
    return render_template("home.html", user=current_user)


@views.route('/delete-note/<id>',methods=['POST','GET'])
@login_required
def delete_note(id):
    Notes = Note.query.filter_by(user_id = id).first()
    db.session.delete(Notes)
    db.session.commit()
    return redirect(url_for('views.home'))

@views.route('/post')
def posts():
    post = Note.query.all()
    return render_template('Posts.html', user=current_user, s=post)

@views.route('/like/<id>',methods=['POST','GET'])
@login_required
def like(id):
    user = User.query.all()
    return redirect(url_for('views.posts'))


@views.route('/image',methods=['POST','GET'])
@login_required
def upload():
    if request.method == 'POST':
        fileobj = request.files['file']
        print(fileobj.filename)
    return render_template('image.html', user=current_user)












# def convertToBinaryData(filename):
#     with open(filename, 'rb') as file:
#         blobData = file.read()
#     return blobData

# @views.route('/upload/',methods=['POST','GET'])
# @login_required
# def upload_image(id):
#     new_image = images()
#     return redirect(url_for('views.posts'))


# db_image = images(image=image.read(),img_type=mintype,image_name =filename ,image_id=current_user.id)