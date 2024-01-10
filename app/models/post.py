from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Post(db.model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return self
