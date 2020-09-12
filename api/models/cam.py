from api import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Cam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    end = db.Column(db.String(120), index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User: {}; End: {}>'.format(self.username, self.end)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)