from flask import render_template
from ..models.post import Post


def index():

    posts = Post.query.all()
    return render_template('post/index', posts=posts)
