from app import db, login
from flask_login import UserMixin
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha1', salt_length=8)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User %r>' %self.username

class Bags(db.Model):
    __tablename__ = 'bags'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Bags {self.name}>'

class Item(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    bag_id = db.Column(db.Integer, db.ForeignKey('bags.id'), nullable=False)
    bag = db.relationship('Bags', backref='items')
    quantity = db.Column(db.Integer, default=1)
    
    def __repr__(self):
        return f'<Item {self.bag.name} x{self.quantity}>'
