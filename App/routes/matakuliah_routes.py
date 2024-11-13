from flask import Blueprint
from flask_restful import Resource, reqparse, fields, marshal_with, abort
from App.extensions import api, db
from App.models.matakuliah import MataKuliahModel

matakuliah_bp = Blueprint('matakuliah', __name__)

matakuliah_fields = {
    'id': fields.Integer,
    'nama': fields.String,
    'kode': fields.String,
    'sks': fields.Integer,
}

matakuliah_parser = reqparse.RequestParser()
matakuliah_parser.add_argument('nama', type=str, required=True)
matakuliah_parser.add_argument('kode', type=str, required=True)
matakuliah_parser.add_argument('sks', type=int, required=True)

class MataKuliahListResource(Resource):
    @marshal_with(matakuliah_fields)
    def get(self):
        return MataKuliahModel.query.all()
    
    @marshal_with(matakuliah_fields)
    def post(self):
        args = matakuliah_parser.parse_args()
        matakuliah = MataKuliahModel(**args)
        db.session.add(matakuliah)
        db.session.commit()
        return matakuliah, 201

class MataKuliahResource(Resource):
    @marshal_with(matakuliah_fields)
    def get(self, id):
        return MataKuliahModel.query.get_or_404(id)
    
    @marshal_with(matakuliah_fields)
    def delete(self, id):
        matakuliah = MataKuliahModel.query.get_or_404(id)
        db.session.delete(matakuliah)
        db.session.commit()
        return '', 204

api.add_resource(MataKuliahListResource, '/api/matakuliah/')
api.add_resource(MataKuliahResource, '/api/matakuliah/<int:id>')