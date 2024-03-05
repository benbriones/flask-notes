from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()

def connect_db(app):
    """Connect to database"""
    app.app_context().push()
    db.app = app
    db.init_app(app)

class User(db.Model):
    """create a User mdoel"""
    __tablename__ = 'users'

    username = db.Column(
        db.String(20),
        primary_key = True
    )

    hashed_password = db.Column(
        db.String(100),
        nullable = False
    )

    email = db.Column(
        db.String(50),
        nullable = False
    )

    first_name = db.Column(
        db.String(30),
        nullable = False
    )

    last_name = db.Column(
        db.String(30),
        nullable = False
    )

    @classmethod
    def register_user(cls, username, pwd, email, first_name, last_name):
        """Register user w/ hashed password and return user"""
        hashed = bcrypt.generate_password_hash(pwd).decode('utf-8')

        return cls(username=username, hashed_password=hashed, email=email,
                   first_name=first_name, last_name=last_name)

    @classmethod
    def authenticate(cls, username, pwd):

