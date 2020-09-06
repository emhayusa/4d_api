from flask import request, jsonify
from flask_restplus import Resource

from ..util.dto import BuildingsDto
from ..util.decorator import admin_token_required, token_required
from ..service.buildings_service import save_new, get_all, get_by_id, get_by_gml_id
from ..util.pagination import get_paginated_list

api =  BuildingsDto.api
_schema =  BuildingsDto.schema
_entry =  BuildingsDto.entry

@api.route('/')
class BuildingsList(Resource):
    @api.doc('list_of_Buildings')
    @api.marshal_list_with(_schema, envelope='data')
    #@token_required
    def get(self):
        """List all Buildings"""
        return get_all()
    #    return jsonify(get_paginated_list(
    #    get_all(), 
    #    '/', 
    #    start=request.args.get('start', 1), 
    #    limit=request.args.get('limit', 20)
    #))

    @api.response(201, 'Building successfully created.')
    @api.doc('create a new building')
    @api.expect(_entry, validate=True)
    @token_required
    def post(self):
        """Creates a new building"""
        data = request.json
        return save_new(data=data)

@api.route('/id/<int:id>')
@api.param('id', 'The building id')
@api.response(404, 'Building not found.')
class Building(Resource):
    @api.doc('get a building')
    @api.marshal_with(_schema)
    #@token_required
    def get(self, id):
        """get a building given its id"""
        row = get_by_id(id)
        if not row:
        	response_object = {
        		'status': 'fail',
        		'message': 'Building ID is not found.',
        	}
        	return response_object, 404
        else:
            return row
			
@api.route('/gml_id/<gml_id>')
@api.param('gml_id', 'The building gml_id')
@api.response(404, 'Building not found.')
class BuildingByGmlId(Resource):
    @api.doc('get a building by its gml_id')
    @api.marshal_with(_schema)
    #@token_required
    def get(self, gml_id):
        """get a building given its gml id"""
        row = get_by_gml_id(gml_id)
        if not row:
        	response_object = {
        		'status': 'fail',
        		'message': 'Building gml_id is not found.',
        	}
        	return response_object, 404
        else:
            return row

@api.route('/gml_id/<gml_id>')
@api.param('gml_id', 'The building gml_id')
@api.response(404, 'Building not found.')
class BuildingByGmlId(Resource):
    @api.doc('get a building by its gml_id')
    @api.marshal_with(_schema)
    #@token_required
    def get(self, gml_id):
        """get a building given its gml id"""
        row = get_by_gml_id(gml_id)
        if not row:
        	response_object = {
        		'status': 'fail',
        		'message': 'Building gml_id is not found.',
        	}
        	return response_object, 404
        else:
            return row