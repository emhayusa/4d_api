from flask import request, jsonify
from flask_restplus import Resource

from ..util.dto import MonitoringAttributeDto, MonitoringPhotoDto, MonitoringVideoDto
from ..util.decorator import admin_token_required, token_required
from ..service.monitoring_attribute_service import save_new, get_all, get_by_id, get_by_user_id, get_by_gml_id, get_by_gml_id_last, get_all_count, verify, get_by_area
from ..service.monitoring_photo_service import save_new_photo, get_all_photo, get_by_id_photo, get_by_user_id_photo, get_by_gml_id_photo, get_by_gml_id_last_photo, get_all_count_photo, verify_photo, get_by_area_photo
from ..service.monitoring_video_service import save_new_video, get_all_video, get_by_id_video, get_by_user_id_video, get_by_gml_id_video, get_by_gml_id_last_video, get_all_count_video, verify_video, get_by_area_video
from ..util.pagination import get_paginated_list

api =  MonitoringAttributeDto.api
_schema =  MonitoringAttributeDto.schema
_entry =  MonitoringAttributeDto.entry
_verify =  MonitoringAttributeDto.verify

api_photo =  MonitoringPhotoDto.api
_schema_photo =  MonitoringPhotoDto.schema
_entry_photo =  MonitoringPhotoDto.entry
_verify_photo =  MonitoringPhotoDto.verify

api_video =  MonitoringVideoDto.api
_schema_video =  MonitoringVideoDto.schema
_entry_video =  MonitoringVideoDto.entry
_verify_video =  MonitoringVideoDto.verify


@api.route('attribute')
class MonitoringAttributeList(Resource):
    @api.doc('list_of_monitorings_attribute')
    @api.marshal_list_with(_schema, envelope='data')
    @admin_token_required
    def get(self):
        """List all monitoring attribute"""
        return get_all()
    #    return jsonify(get_paginated_list(
    #    get_all(), 
    #    '/', 
    #    start=request.args.get('start', 1), 
    #    limit=request.args.get('limit', 20)
    #))

    @api.response(201, 'Monitoring attribute successfully created.')
    @api.doc('create a new monitoring attribute')
    @api.expect(_entry, validate=True)
    @token_required
    def post(self):
        """Creates a new Monitoring attribute"""
        data = request.json
        return save_new(data=data)


@api.route('attribute/verify/')
class AttributeVerification(Resource):
    @api.response(202, 'Attribute successfully verified.')
    @api.response(404, 'Not Found')
    @api.response(503, 'Service Unavailable')
    @api.doc('Verify a new Attribute')
    @api.expect(_verify, validate=True)
    @token_required
    def post(self):
        """Verify a new Attribute """
        data = request.json
        return verify(data=data)
		
@api.route('attribute/id/<int:id>')
@api.param('id', 'The Monitoring attribute id')
@api.response(404, 'Monitoring attribute not found.')
class MonitoringAttribute(Resource):
    @api.doc('get a monitoring attribute')
    @api.marshal_with(_schema)
    @token_required
    def get(self, id):
        """get a monitoring attribute given its id"""
        row = get_by_id(id)
        if not row:
        	response_object = {
        		'status': 'fail',
        		'message': 'Monitoring attribute ID is not found.',
        	}
        	return response_object, 404
        else:
            return row

@api.route('attribute/user/<user_id>')
@api.response(404, 'Monitoring attribute not found.')
class MonitoringAttributeListByUser(Resource):
    @api.doc('list_of_monitoring_attribute_by_user_id')
    @api.marshal_list_with(_schema, envelope='data')
    @token_required
    def get(self, user_id):
        """List all monitoring attribute by user_id"""
        return get_by_user_id(user_id)
		
@api.route('attribute/gml_list/<gml_id>')
@api.response(404, 'Monitoring attribute not found.')
class MonitoringAttributeListByGMLID(Resource):
    @api.doc('list_of_monitoring_attribute_by_gml_id')
    @api.marshal_list_with(_schema, envelope='data')
    def get(self, gml_id):
        """List all monitoring attribute by gml id"""
        return get_by_gml_id(gml_id)
		
@api.route('attribute/gml/<gml_id>')
@api.param('gml_id', 'The Monitoring attribute gml_id')
@api.response(404, 'Monitoring attribute not found.')
class MonitoringAttributeByGMLID(Resource):
    @api.doc('get a monitoring attribute by gml id')
    @api.marshal_with(_schema)
    def get(self, gml_id):
        """get a monitoring attribute given its gml_id"""
        row = get_by_gml_id_last(gml_id)
        if not row:
        	response_object = {
        		'status': 'fail',
        		'message': 'Monitoring attribute gml id is not found.',
        	}
        	return response_object, 404
        else:
            return row

@api.route('attribute/area/<int:id>')
@api.response(404, 'The Monitoring Attribute List not found.')
class MonitoringAttributeListByArea(Resource):
    @api.doc('list_of_monitoring_attribute_by_area_id')
    @api.marshal_list_with(_schema, envelope='data')
    #@token_required
    def get(self, id):
        """List all monitoring attribute by area id"""
        return get_by_area(id)
		
@api_photo.route('photo')
class MonitoringPhotoList(Resource):
    @api_photo.doc('list_of_monitorings_photo')
    @api_photo.marshal_list_with(_schema_photo, envelope='data')
    @admin_token_required
    def get(self):
        """List all monitoring photo"""
        return get_all_photo()
    #    return jsonify(get_paginated_list(
    #    get_all(), 
    #    '/', 
    #    start=request.args.get('start', 1), 
    #    limit=request.args.get('limit', 20)
    #))

    @api_photo.response(201, 'Monitoring photo successfully created.')
    @api_photo.doc('create a new monitoring photo')
    @api_photo.expect(_entry_photo, validate=True)
    @token_required
    def post(self):
        """Creates a new Monitoring photo"""
        data = request.json
        return save_new_photo(data=data)


@api_photo.route('photo/verify/')
class PhotoVerification(Resource):
    @api_photo.response(202, 'Photo successfully verified.')
    @api_photo.response(404, 'Not Found')
    @api_photo.response(503, 'Service Unavailable')
    @api_photo.doc('Verify a new Photo')
    @api_photo.expect(_verify_photo, validate=True)
    @token_required
    def post(self):
        """Verify a new Photo """
        data = request.json
        return verify_photo(data=data)
		
@api_photo.route('photo/id/<int:id>')
@api_photo.param('id', 'The Monitoring photo id')
@api_photo.response(404, 'Monitoring photo not found.')
class MonitoringPhoto(Resource):
    @api_photo.doc('get a monitoring photo')
    @api_photo.marshal_with(_schema_photo)
    @token_required
    def get(self, id):
        """get a monitoring photo given its id"""
        row = get_by_id_photo(id)
        if not row:
        	response_object = {
        		'status': 'fail',
        		'message': 'Monitoring photo ID is not found.',
        	}
        	return response_object, 404
        else:
            return row

@api_photo.route('photo/user/<user_id>')
@api_photo.response(404, 'Monitoring photo not found.')
class MonitoringPhotoListByUser(Resource):
    @api_photo.doc('list_of_monitoring_photo_by_username')
    @api_photo.marshal_list_with(_schema_photo, envelope='data')
    @token_required
    def get(self, user_id):
        """List all monitoring photo by username"""
        return get_by_user_id_photo(user_id)

@api_photo.route('photo/gml_list/<gml_id>')
@api_photo.response(404, 'Monitoring photo list not found.')
class MonitoringPhotoListByGMLID(Resource):
    @api_photo.doc('list_of_monitoring_photo_list_by_gml_id')
    @api_photo.marshal_list_with(_schema_photo, envelope='data')
    def get(self, gml_id):
        """List all monitoring photo by gml id"""
        return get_by_gml_id_photo(gml_id)
		
@api_photo.route('photo/gml/<gml_id>')
@api_photo.param('gml_id', 'The Monitoring photo gml_id')
@api_photo.response(404, 'Monitoring photo not found.')
class MonitoringPhotoByGMLID(Resource):
    @api_photo.doc('get a monitoring photo by gml id')
    @api_photo.marshal_with(_schema_photo)
    def get(self, gml_id):
        """get a monitoring photo given its gml_id"""
        row = get_by_gml_id_last_photo(gml_id)
        if not row:
        	response_object = {
        		'status': 'fail',
        		'message': 'Monitoring photo gml id is not found.',
        	}
        	return response_object, 404
        else:
            return row

@api_photo.route('photo/area/<int:id>')
@api_photo.response(404, 'The Monitoring Photo List not found.')
class MonitoringPhotoListByArea(Resource):
    @api_photo.doc('list_of_monitoring_photo_by_area_id')
    @api_photo.marshal_list_with(_schema_photo, envelope='data')
    #@token_required
    def get(self, id):
        """List all monitoring photo by area id"""
        return get_by_area_photo(id)
		
		
@api_video.route('video')
class MonitoringVideoList(Resource):
    @api_video.doc('list_of_monitorings_video')
    @api_video.marshal_list_with(_schema_video, envelope='data')
    @admin_token_required
    def get(self):
        """List all monitoring video"""
        return get_all_video()
    #    return jsonify(get_paginated_list(
    #    get_all(), 
    #    '/', 
    #    start=request.args.get('start', 1), 
    #    limit=request.args.get('limit', 20)
    #))

    @api_video.response(201, 'Monitoring video successfully created.')
    @api_video.doc('create a new monitoring video')
    @api_video.expect(_entry_video, validate=True)
    @token_required
    def post(self):
        """Creates a new Monitoring video"""
        data = request.json
        return save_new_video(data=data)
		

@api_video.route('video/verify/')
class VideoVerification(Resource):
    @api_video.response(202, 'Video successfully verified.')
    @api_video.response(404, 'Not Found')
    @api_video.response(503, 'Service Unavailable')
    @api_video.doc('Verify a new Video')
    @api_video.expect(_verify_video, validate=True)
    @token_required
    def post(self):
        """Verify a new Video """
        data = request.json
        return verify_video(data=data)
		

@api_video.route('video/id/<int:id>')
@api_video.param('id', 'The Monitoring video id')
@api_video.response(404, 'Monitoring video not found.')
class MonitoringVideo(Resource):
    @api_video.doc('get a monitoring video')
    @api_video.marshal_with(_schema_video)
    @token_required
    def get(self, id):
        """get a monitoring video given its id"""
        row = get_by_id_video(id)
        if not row:
        	response_object = {
        		'status': 'fail',
        		'message': 'Monitoring video ID is not found.',
        	}
        	return response_object, 404
        else:
            return row

@api_video.route('video/user/<username>')
@api_video.response(404, 'Monitoring video not found.')
class MonitoringVideoListByUser(Resource):
    @api_video.doc('list_of_monitoring_video_by_username')
    @api_video.marshal_list_with(_schema_video, envelope='data')
    @token_required
    def get(self, username):
        """List all monitoring video by username"""
        return get_by_user_id_video(username)
	
@api_video.route('video/gml_list/<gml_id>')
@api_video.response(404, 'Monitoring video list not found.')
class MonitoringVideoListByGMLID(Resource):
    @api_video.doc('list_of_monitoring_video_list_by_gml_id')
    @api_video.marshal_list_with(_schema_video, envelope='data')
    def get(self, gml_id):
        """List all monitoring video by gml id"""
        return get_by_gml_id_video(gml_id)
		
@api_video.route('video/gml/<gml_id>')
@api_video.param('gml_id', 'The Monitoring video gml_id')
@api_video.response(404, 'Monitoring video not found.')
class MonitoringVideoByGMLID(Resource):
    @api_video.doc('get a monitoring video by gml id')
    @api_video.marshal_with(_schema_video)
    def get(self, gml_id):
        """get a monitoring video given its gml_id"""
        row = get_by_gml_id_last_video(gml_id)
        if not row:
        	response_object = {
        		'status': 'fail',
        		'message': 'Monitoring video gml id is not found.',
        	}
        	return response_object, 404
        else:
            return row

@api_video.route('video/area/<int:id>')
@api_video.response(404, 'The Monitoring Video List not found.')
class MonitoringPhotoListByArea(Resource):
    @api_video.doc('list_of_monitoring_video_by_area_id')
    @api_video.marshal_list_with(_schema_video, envelope='data')
    #@token_required
    def get(self, id):
        """List all monitoring video by area id"""
        return get_by_area_video(id)
		