from flask import Blueprint, jsonify, abort, request
from ..models import Application, User, db
import datetime

bp = Blueprint('applications', __name__, url_prefix='/applications')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    applications = Application.query.all() # ORM performs SELECT query
    result = []
    for a in applications:
        result.append(a.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    a = Application.query.get_or_404(id, "Application not found")
    return jsonify(a.serialize())

@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content

    required_fields = ['user_id', 'company_id']
    if not all(field in request.json for field in required_fields):
        return abort(400, description="missing required fields")
    
    # user with id of user_id must exist
    user = User.query.get_or_404(request.json['user_id'], "User not found")

    created_at = request.json.get('created_at', datetime.datetime.utcnow().isoformat())

    # try:
    #     created_at = datetime.datetime.fromisoformat(request.json['created_at'])
    # except ValueError:
    #     return abort(400, description="Invalid created_at format")

    # construct Tweet
    a = Application(
        user_id=user.id,
        position=request.json['position'],
        notes=request.json['notes'],
        created_at=created_at,
        company_id=request.json['company_id']
    )
    db.session.add(a) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(a.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    a = Application.query.get_or_404(id, "Application not found")
    try:
        db.session.delete(a) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)
    
# @bp.route('/<int:id>/liking_users', methods=['GET'])
# def liking_users(id: int):
#     t = Tweet.query.get_or_404(id)
#     result = []
#     for u in t.liking_users:
#         result.append(u.serialize())
#     return jsonify(result)
    



@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    a = Application.query.get_or_404(id)
    if 'position' in request.json:
        a.position = request.json['position']
    if 'notes' in request.json:
        a.notes = request.json['notes']
    if 'company_id' in request.json:
        a.company_id = request.json['company_id']

    try:
        db.session.commit()
        return jsonify(a.serialize())
    except:
        return jsonify(False)