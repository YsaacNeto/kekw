from flask import render_template
from models import Post


def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('')
