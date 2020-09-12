from api import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created = db.Column(db.DateTime)

    def __init__(self, username, email, password):
        self.id = User[-1]['id']+1
        self.username = username
        self.email = email
        self.created =  datetime.now()
        self.password_hash = self.set_password(password)

    def __repr__(self):
        return '<{} User: {}, email: {}>'.format(self.id, self.username, self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)