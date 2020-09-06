from flask import request, jsonify
from flask_restplus import Resource

from ..util.dto import CityGmlDto
from ..util.decorator import admin_token_required, token_required
from ..service.city_gml_service import save_new, get_all, get_by_id, get_by_username, get_by_area, verify
from ..util.pagination import get_paginated_list

api =  CityGmlDto.api
_schema =  CityGmlDto.schema
_entry =  CityGmlDto.entry
_verify =  CityGmlDto.verify

@api.route('/')
class CityGmlList(Resource):
    @api.doc('list_of_CityGmls')
    @api.marshal_list_with(_schema, envelope='data')
    @token_required
    def get(self):
        """List all CityGmls"""
        return get_all()
    #    return jsonify(get_paginated_list(
    #    get_all(), 
    #    '/', 
    #    start=request.args.get('start', 1), 
    #    limit=request.args.get('limit', 20)
    #))

    @api.response(201, 'CityGml successfully created.')
    @api.doc('create a new CityGml')
    @api.expect(_entry, validate=True)
    @token_required
    def post(self):
        """Creates a new CityGml"""
        data = request.json
        return save_new(data=data)

@api.route('/verify/')
class CityGmlVerification(Resource):
    @api.response(202, 'CityGml successfully verified.')
    @api.response(404, 'Not Found')
    @api.response(503, 'Service Unavailable')
    @api.doc('Verify a new CityGml')
    @api.expect(_verify, validate=True)
    def post(self):
        """Verify a new Gml """
        data = request.json
        return verify(data=data)
		
@api.route('/id/<int:id>')
@api.param('id', 'The CityGml id')
@api.response(404, 'CityGml not found.')
class CityGml(Resource):
    @api.doc('get a CityGml')
    @api.marshal_with(_schema)
    @token_required
    def get(self, id):
        """get a Gml given its id"""
        row = get_by_id(id)
        if not row:
        	response_object = {
        		'status': 'fail',
        		'message': 'CityGml ID is not found.',
        	}
        	return response_object, 404
        else:
            return row

@api.route('/username/<username>')
@api.response(404, 'The CityGml List not found.')
class CityGmlListByUser(Resource):
    @api.doc('list_of_CityGml_by_username')
    @api.marshal_list_with(_schema, envelope='data')
    @token_required
    def get(self, username):
        """List all CityGmls by username"""
        return get_by_username(username)
		
@api.route('/area/<int:id>')
@api.response(404, 'The City Gml List not found.')
class CityGmlListByArea(Resource):
    @api.doc('list_of_citygml_by_area_id')
    @api.marshal_list_with(_schema, envelope='data')
    #@token_required
    def get(self, id):
        """List all city gmls by area id"""
        return get_by_area(id)