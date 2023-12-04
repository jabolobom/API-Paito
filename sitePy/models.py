from sitePy import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(userID):
    return user.query.get(int(userID))

class user(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False, unique=True)
    passw = database.Column(database.String, nullable=False)
    imagem = database.relationship('foto', backref='user', lazy=True)

class foto(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    img = database.Column(database.String, default="default.png")
    crDate = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    ownerID = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
