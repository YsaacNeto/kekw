from flask import Blueprint
from app.views import home, post

main = Blueprint('main', __name__)

main.add_url_rule('/', view_func=home)
main.add_url_rule('/posts', view_func=post)
