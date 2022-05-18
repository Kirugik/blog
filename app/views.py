from flask import Blueprint, render_template, request, redirect, url_for, flash  
from flask_login import login_required, current_user  
from .models import Post, User, Comment, Like 
from . import db  
from .requests import get_quotes 

views = Blueprint("views", __name__) 

@views.route("/")
@views.route("/home")
# @login_required   
def home():
    posts = Post.query.all()
    quote = get_quotes() 
    
    return render_template('home.html', user=current_user, posts=posts, quote=quote)



@views.route("/create-post", methods=['GET', 'POST'])
@login_required   
def create_post():
    if request.method == 'POST':
        title = request.form.get('title') 
        text = request.form.get('text')
        
        if not text:
            flash('Post cannot be empty.', category='error') 
        else:
            # creating a new post and saving it to db 
            post = Post(title=title, text=text, author=current_user.id) 
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



@views.route("/posts/<username>")
@login_required   
def posts(username):
    user = User.query.filter_by(username=username).first()
    quote = get_quotes() 

    if not user:
        flash("No user with that username.", category='error')
        return redirect(url_for('views.home')) 
    posts = user.posts 
    return render_template('posts.html', user=current_user, posts=posts, username=username, quote=quote) 



@views.route("/create-comment/<post_id>", methods=['POST']) 
@login_required   
def create_comment(post_id):
    text = request.form.get('text') 

    # check if a comment has been typed in the comment input
    if not text:
        flash('Comment cannot be empty.', category='error')
    # if there is a comment typed ...
    else:
        # make sure there is a post for which the comment is being made 
        post = Post.query.filter_by(id=post_id)
        # if there is a post ...
        if post:
            # creating a new comment and saving to db
            comment = Comment(text=text, author=current_user.id, post_id=post_id) 
            db.session.add(comment)
            db.session.commit()

        # if there is no post ...
        else:
            flash('Post does not exist.', category='error')


    return redirect(url_for('views.home'))




@views.route("/delete-comment/<comment_id>") 
@login_required   
def delete_comment(comment_id):
    # Check if the comment exists in the db
    comment = Comment.query.filter_by(id=comment_id).first()
    # if there is no comment...
    if not comment: 
        flash('Comment does not exist.', category='error')
    # if there is a comment, check if the current user(the logged in user) is the author of either the post or the comment
    # we only want the comment to be deleted by either the author of the post or author of the comment
    elif current_user.id != comment.author and current_user.id != comment.post.author:
        flash('You are not allowed to delete this comment.', category='error') 
    # if there is comment and the current user(logged in user) is either the author of the post or author of the comment, delete the comment from db 
    else:
        db.session.delete(comment)
        db.session.commit()
        flash('Comment deleted!', category='success')
    return redirect(url_for('views.home')) 



@views.route("/like-post/<post_id>", methods=['GET'])  
@login_required   
def like(post_id):
    # Check if there is a post and a like in the db
    post = Post.query.filter_by(id=post_id)
    like = Like.query.filter_by(author=current_user.id, post_id=post_id).first()

    # if there is no post...
    if not post:
        flash('Post does not exist.', category='error')
    # if there is a post with a like, remove the like
    elif like:
        db.session.delete(like)
        db.session.commit()
    # if there is a post with or without a like, add a like 
    else:
        like = Like(author=current_user.id, post_id=post_id)
        db.session.add(like) 
        db.session.commit()
    return redirect(url_for('views.home')) 



@views.route('/profile/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    text = Post.query.filter_by(author=author).all()

    if user is None:
        abort(404)
    
    return render_template("profile.html", user = user) 