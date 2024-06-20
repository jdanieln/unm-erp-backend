from ..database import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename_ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(1280), nullable=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def serialize(self):
       return {
            'id': self.id,
            'username': self.username
        }
    