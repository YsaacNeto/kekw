from flask import render_template
from ..models.user import User


def index():
    users = User.query.all()
    return render_template('user/index', users=users)
