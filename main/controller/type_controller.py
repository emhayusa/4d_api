from flask import request, jsonify
from flask_restplus import Resource

from ..util.dto import TypeDto
from ..util.decorator import admin_token_required, token_required
from ..service.type_service import save_new, get_all, get_by_id
from ..util.pagination import get_paginated_list

api =  TypeDto.api
_schema =  TypeDto.schema
_entry =  TypeDto.entry

@api.route('/')
class TypeList(Resource):
    @api.doc('list_of_types')
    @api.marshal_list_with(_schema, envelope='data')
    #@admin_token_required
    def get(self):
        """List all types"""
        return get_all()
    #    return jsonify(get_paginated_list(
    #    get_all(), 
    #    '/', 
    #    start=request.args.get('start', 1), 
    #    limit=request.args.get('limit', 20)
    #))

    @api.response(201, 'Type successfully created.')
    @api.response(409, 'Type already Exists')
    @api.doc('create a new type')
    @api.expect(_entry, validate=True)
    @admin_token_required
    def post(self):
        """Creates a new Type"""
        data = request.json
        return save_new(data=data)

@api.route('/id/<int:id>')
@api.param('id', 'The Type id')
@api.response(404, 'Type not found.')
class Type(Resource):
    @api.doc('get a type')
    @api.marshal_with(_schema)
    @admin_token_required
    def get(self, id):
        """get a type given its id"""
        row = get_by_id(id)
        if not row:
        	response_object = {
        		'status': 'fail',
        		'message': 'Type ID is not found.',
        	}
        	return response_object, 404
        else:
            return row