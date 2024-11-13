from flask import Blueprint, request
from flask_restful import Resource, reqparse, fields, marshal_with, abort
from App.extensions import api, db
from App.models.user import UserModel

user_bp = Blueprint('user', __name__)

user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
}

# Parser untuk request
user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, required=True, help="Name cannot be blank")
user_parser.add_argument('email', type=str, required=True, help="Email cannot be blank")

class UsersResource(Resource):
    @marshal_with(user_fields)
    def get(self):
        return UserModel.query.all()
    
    @marshal_with(user_fields)
    def post(self):
        args = user_parser.parse_args()
        user = UserModel(name=args["name"], email=args["email"])
        db.session.add(user)
        db.session.commit()
        return user, 201

class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self, id):
        user = UserModel.query.get_or_404(id)
        return user

    @marshal_with(user_fields)
    def put(self, id):
        args = user_parser.parse_args()
        user = UserModel.query.get_or_404(id)
        user.name = args["name"]
        user.email = args["email"]
        db.session.commit()
        return user

    @marshal_with(user_fields)
    def patch(self, id):
        args = user_parser.parse_args()
        user = UserModel.query.get_or_404(id)
        
        existing_name = UserModel.query.filter(
            UserModel.name == args["name"],
            UserModel.id != id
        ).first()
        if existing_name:
            abort(400, message=f"Name {args['name']} already exists")

        existing_email = UserModel.query.filter(
            UserModel.email == args["email"],
            UserModel.id != id
        ).first()
        if existing_email:
            abort(400, message=f"Email {args['email']} already exists")
            
        try:
            user.name = args["name"]
            user.email = args["email"]
            db.session.commit()
            return user
        except Exception as e:
            db.session.rollback()
            abort(400, message=str(e))

    @marshal_with(user_fields)
    def delete(self, id):
        user = UserModel.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

class UserSearchResource(Resource):
    @marshal_with(user_fields)
    def get(self):
        name = request.args.get('name')
        email = request.args.get('email')
        
        query = UserModel.query
        if name:
            query = query.filter(UserModel.name.like(f"%{name}%"))
        if email:
            query = query.filter(UserModel.email.like(f"%{email}%"))
        
        users = query.all()
        if not users:
            abort(404, message="No users found matching criteria")
        return users

class UserEmailsResource(Resource):
    def get(self):
        emails = [user.email for user in UserModel.query.all()]
        return {"emails": emails}

class UserCountResource(Resource):
    def get(self):
        count = UserModel.query.count()
        return {"total_users": count}

class UserPaginationResource(Resource):
    @marshal_with(user_fields)
    def get(self, page):
        limit = request.args.get('limit', default=5, type=int)
        users = UserModel.query.paginate(page=page, per_page=limit, error_out=False).items
        return users

api.add_resource(UsersResource, '/api/users/')
api.add_resource(UserResource, '/api/users/<int:id>')
api.add_resource(UserSearchResource, '/api/users/search')
api.add_resource(UserEmailsResource, '/api/users/emails')
api.add_resource(UserCountResource, '/api/users/count')
api.add_resource(UserPaginationResource, '/api/users/page/<int:page>')