from flask import Blueprint, jsonify, abort, request
from ..models import User, db
from email_validator import validate_email, EmailNotValidError
import hashlib
import secrets

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    users = User.query.all() # ORM performs SELECT query
    result = []
    for u in users:
        result.append(u.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id, "User not found")
    return jsonify(u.serialize())

@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'username' not in request.json or 'password' not in request.json or 'email' not in request.json:
        return abort(400)
    # construct Tweet
    if len(request.json['username']) < 3 or len(request.json['password']) < 8 or len(request.json['email']) < 5:
        return abort(400)
    u = User(
        username=request.json['username'],
        email=request.json['email'],
        password=scramble(request.json['password'])
    )
    db.session.add(u) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(u.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id, "User not found")
    try:
        db.session.delete(u) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)
    
@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    u = User.query.get_or_404(id)
    if 'email' not in request.json and 'password' not in request.json:
        return abort(400)
    if 'email' in request.json:
        try: 
            v = validate_email(request.json['email'])
            u.email = v["email"]
        except EmailNotValidError as e:
            return abort(400, description=str(e))
    if 'password' in request.json:
        if len(request.json['password']) < 3:
            return abort(400)
        u.password = scramble(request.json['password'])
    try:
        db.session.commit()
        return jsonify(u.serialize())
    except:
        return jsonify(False)
    
@bp.route('/<int:id>/applications', methods=['GET'])
def applications(id: int):
    u = User.query.get_or_404(id)
    result = []
    for t in u.liked_tweets:
        result.append(t.serialize())
    return jsonify(result)
