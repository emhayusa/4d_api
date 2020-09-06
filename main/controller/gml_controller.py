from flask import request, jsonify
from flask_restplus import Resource

from ..util.dto import GmlDto
from ..util.decorator import admin_token_required, token_required
from ..service.gml_service import save_new, get_all, get_by_id, get_by_username, get_by_area, verify
from ..util.pagination import get_paginated_list

api =  GmlDto.api
_schema =  GmlDto.schema
_entry =  GmlDto.entry
_verify =  GmlDto.verify

@api.route('/')
class GmlList(Resource):
    @api.doc('list_of_Gmls')
    @api.marshal_list_with(_schema, envelope='data')
    @token_required
    def get(self):
        """List all Gmls"""
        return get_all()
    #    return jsonify(get_paginated_list(
    #    get_all(), 
    #    '/', 
    #    start=request.args.get('start', 1), 
    #    limit=request.args.get('limit', 20)
    #))

    @api.response(201, 'Gml successfully created.')
    @api.response(409, 'Gml already Exists')
    @api.doc('create a new Gml')
    @api.expect(_entry, validate=True)
    @token_required
    def post(self):
        """Creates a new Gml"""
        data = request.json
        return save_new(data=data)

@api.route('/verify/')
class GmlVerification(Resource):
    @api.response(202, 'Gml successfully verified.')
    @api.response(404, 'Not Found')
    @api.response(503, 'Service Unavailable')
    @api.doc('Verify a new gml')
    @api.expect(_verify, validate=True)
    def post(self):
        """Verify a new Gml """
        data = request.json
        return verify(data=data)
		
@api.route('/id/<int:id>')
@api.param('id', 'The Gml id')
@api.response(404, 'Gml not found.')
class Gml(Resource):
    @api.doc('get a Gml')
    @api.marshal_with(_schema)
    @token_required
    def get(self, id):
        """get a Gml given its id"""
        row = get_by_id(id)
        if not row:
        	response_object = {
        		'status': 'fail',
        		'message': 'Gml ID is not found.',
        	}
        	return response_object, 404
        else:
            return row

@api.route('/username/<username>')
@api.response(404, 'The Gml List not found.')
class GmlListByUser(Resource):
    @api.doc('list_of_gml_by_username')
    @api.marshal_list_with(_schema, envelope='data')
    @token_required
    def get(self, username):
        """List all gmls by user username"""
        return get_by_username(username)
		
@api.route('/area/<int:id>')
@api.response(404, 'The Gml List not found.')
class GmlListByArea(Resource):
    @api.doc('list_of_gml_by_area_id')
    @api.marshal_list_with(_schema, envelope='data')
    @token_required
    def get(self, id):
        """List all gmls by area id"""
        return get_by_area(id)