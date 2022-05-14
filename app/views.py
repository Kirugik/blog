from flask import Blueprint, render_template, request, redirect, url_for, flash  
from flask_login import login_required, current_user  
from .models import Post, User, Comment, Like 
from . import db  

views = Blueprint("views", __name__) 

@views.route("/")
@views.route("/home")
@login_required   
def home():
    posts = Post.query.all()
    return render_template('home.html', user=current_user, posts=posts)



@views.route("/create-post", methods=['GET', 'POST'])
@login_required   
def create_post():
    if request.method == 'POST':
        text = request.form.get('text')

        if not text:
            flash('Post cannot be empty.', category='error') 
        else:
            # creating a new post and saving it to db 
            post = Post(text=text, author=current_user.id) 
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('create_post.html', user=current_user)  



@views.route("/delete-post/<id>")
@login_required   
def delete_post(id): 
    post = Post.query.filter_by(id=id).first()

    if not post:
        flash("Post does not exist.", category='error')
    elif current_user.id != post.id:
        flash("You cannot delete this post.", category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted", category='success')
    return redirect(url_for('views.home')) 