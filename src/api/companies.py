from flask import Blueprint, jsonify, abort, request
from ..models import Application, Company, User, db

bp = Blueprint('companies', __name__, url_prefix='/companies')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    companies = Company.query.all() # ORM performs SELECT query
    result = []
    for c in companies:
        result.append(c.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    c = Company.query.get_or_404(id, "Company not found")
    return jsonify(c.serialize())

@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'company_name' not in request.json:
        return abort(400)
    
    # I don't think this is needed since companies are only connected to users in that the user's applications are connected to the companies...
    # User.query.get_or_404(request.json['user_id'], "Company not found")

    # construct Company
    c = Company(
        company_name=request.json['company_name'],
        notes=request.json.get('notes', None),
        contact_name=request.json.get('contact_name', None),
        contact_email=request.json.get('contact_email', None)
    )
    db.session.add(c) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(c.serialize())

@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    c = Company.query.get_or_404(id)
    if 'company_name' in request.json:
        c.company_name = request.json['company_name']
    if 'notes' in request.json:
        c.notes = request.json['notes']
    if 'contact_name' in request.json:
        c.contact_name = request.json['contact_name']
    if 'contact_email' in request.json:
        c.contact_email = request.json['contact_email']

    try:
        db.session.commit()
        return jsonify(c.serialize())
    except:
        return jsonify(False)

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