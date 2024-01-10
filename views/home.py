from flask import render_template


def home():
    title = 'home'
    return render_template('home.html', title=title)
