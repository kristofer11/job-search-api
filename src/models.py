import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, username:str, email:str, password:str):
        self.username = username
        self.email = email
        self.set_password(password)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
        
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Application(db.Model):
    __tablename__ = 'applications'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    position = db.Column(db.String(128), nullable=True)
    notes = db.Column(db.String(128), nullable=True)
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=datetime.datetime.utcnow,
        nullable=False
    )
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    
    def __init__(self, position:str, user_id:int, notes:str, created_at:datetime, company_id:int):
        self.position = position
        self.user_id = user_id
        self.notes = notes
        self.created_at = created_at
        self.company_id = company_id

    def serialize(self):
        return {
            'id': self.id,
            'position': self.position,
            'notes': self.notes,
            'created_at': self.created_at.isoformat(),
            'user_id': self.user_id,
            'company_id': self.company_id
        }  

# Probably don't need an association table if users aren't directly connected to companies. 
# Since we will only track applications and not other inquiry forms, applications will be 
# associated with both the user and the company.
      
# user_company_association = db.Table(
#     'user_company_association',
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
#     db.Column('company_id', db.Integer, db.ForeignKey('companies.id'))
# )

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String(128), unique=True, nullable=False)
    notes = db.Column(db.String(128), nullable=True)
    contact_name = db.Column(db.String(128), unique=False, nullable=True)
    contact_email = db.Column(db.String(128), unique=False, nullable=True)


# Probably not needed since association table will not be used:
    # users = db.relationship('User', secondary='user_company_association', back_populates='companies')

    def __init__(self, company_name:str, notes:str, contact_name:str, contact_email:str):
        self.company_name = company_name
        self.notes = notes
        self.contact_name = contact_name
        self.contact_email = contact_email

    def serialize(self):
        return {
            'id': self.id,
            'company_name': self.company_name,
            'notes': self.notes,
            'contact_name': self.contact_name,
            'contact_email': self.contact_email
        }
    
