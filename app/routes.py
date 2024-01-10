from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/', defaults={'page': 'index'})
@main.route('/<page>')
def show(page):
    try:
        return render_template(f'{page}.html')
    except TemplateNotFound:
        abort(404)
