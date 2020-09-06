from flask import request, jsonify
from flask_restplus import Resource

from ..util.dto import AreaDto
from ..util.decorator import admin_token_required, token_required
from ..service.area_service import save_new, get_all, get_by_id
from ..util.pagination import get_paginated_list

api =  AreaDto.api
_schema =  AreaDto.schema
_entry =  AreaDto.entry

@api.route('/')
class AreaList(Resource):
    @api.doc('list_of_areas')
    @api.marshal_list_with(_schema, envelope='data')
    #@admin_token_required
    def get(self):
        """List all area"""
        return get_all()
    #    return jsonify(get_paginated_list(
    #    get_all(), 
    #    '/', 
    #    start=request.args.get('start', 1), 
    #    limit=request.args.get('limit', 20)
    #))

    @api.response(201, 'Area successfully created.')
    @api.response(409, 'Area already Exists')
    @api.doc('create a new area')
    @api.expect(_entry, validate=True)
    @admin_token_required
    def post(self):
        """Creates a new Area """
        data = request.json
        return save_new(data=data)

@api.route('/id/<int:id>')
@api.param('id', 'The Area id')
@api.response(404, 'Area not found.')
class Area(Resource):
    @api.doc('get a area')
    @api.marshal_with(_schema)
    @admin_token_required
    def get(self, id):
        """get a area given its id"""
        row = get_by_id(id)
        if not row:
        	response_object = {
        		'status': 'fail',
        		'message': 'Area ID is not found.',
        	}
        	return response_object, 404
        else:
            return row