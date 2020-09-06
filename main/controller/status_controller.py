from flask import request, jsonify
from flask_restplus import Resource

from ..util.dto import StatusDto
from ..util.decorator import admin_token_required, token_required
from ..service.status_service import save_new, get_all, get_by_id
from ..util.pagination import get_paginated_list

api =  StatusDto.api
_schema =  StatusDto.schema
_entry =  StatusDto.entry

@api.route('/')
class StatusList(Resource):
    @api.doc('list_of_status')
    @api.marshal_list_with(_schema, envelope='data')
    #@admin_token_required
    def get(self):
        """List all Statuss"""
        return get_all()
    #    return jsonify(get_paginated_list(
    #    get_all(), 
    #    '/', 
    #    start=request.args.get('start', 1), 
    #    limit=request.args.get('limit', 20)
    #))

    @api.response(201, 'Status successfully created.')
    @api.response(409, 'Status already Exists')
    @api.doc('create a new status')
    @api.expect(_entry, validate=True)
    @admin_token_required
    def post(self):
        """Creates a new Status"""
        data = request.json
        return save_new(data=data)

@api.route('/id/<int:id>')
@api.param('id', 'The Status id')
@api.response(404, 'Status not found.')
class Status(Resource):
    @api.doc('get a status')
    @api.marshal_with(_schema)
    @admin_token_required
    def get(self, id):
        """get a Status given its id"""
        row = get_by_id(id)
        if not row:
        	response_object = {
        		'status': 'fail',
        		'message': 'Status ID is not found.',
        	}
        	return response_object, 404
        else:
            return row