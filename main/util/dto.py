from flask_restplus import Namespace, fields

	
class StatusDto:
    api = Namespace('status', description='status related operations')
    schema = api.model('status', {
        'id': fields.Integer(dump_only=True),
        'status_name': fields.String(required=True, description='status name')
    })
    entry = api.model('status_entry', {
        'status_name': fields.String(required=True, description='status name')
    })

	
class TypeDto:
    api = Namespace('type', description='type related operations')
    schema = api.model('type', {
        'id': fields.Integer(dump_only=True),
        'type_name': fields.String(required=True, description='type name')
    })
    entry = api.model('type_entry', {
        'type_name': fields.String(required=True, description='type name')
    })

class AreaDto:
    api = Namespace('area', description='area related operations')
    schema = api.model('area', {
        'id': fields.Integer(dump_only=True),
        'area_name': fields.String(required=True, description='area_name')
    })
    entry = api.model('area_entry', {
        'area_name': fields.String(required=True, description='area_name')
    })
	
class UserDto:
    api = Namespace('user', description='user related operations')
    schema = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'public_id': fields.String(description='user Identifier'),
        'type' : fields.Nested(TypeDto().schema, required=True),
        'area' : fields.Nested(AreaDto().schema, required=True)
    })
    user = api.model('user', {
		'type_id' : fields.Integer(required=True, description='type id'),
		'area_id' : fields.Integer(required=True, description='area id'),
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'username': fields.String(required=True, description='The username'),
        'password': fields.String(required=True, description='The user password ')
    })



class GmlDto:
    api = Namespace('gml', description='gml related operations')
    schema = api.model('gml', {
        'id': fields.Integer(dump_only=True),
        #'contributor' : fields.Nested(UserDto().schema, required=True),
        'contributor': fields.String(required=True, description='contributor username'),
        'building_name': fields.String(required=True, description='building name'),
        'city_gml_file': fields.String(required=True, description='city gml file name'),
        'uploaded_on': fields.DateTime(required=True, description='uploaded time'),
        'verified_on': fields.DateTime(required=True, description='verified time'),
        'validator': fields.String(required=True, description='validator username'),
        #'validator' : fields.Nested(UserDto().schema, required=True),
        'reason': fields.String(required=True, description='reason'),
        'area' : fields.Nested(AreaDto().schema, required=True),
        'status' : fields.Nested(StatusDto().schema, required=True)
    })
    entry = api.model('gml_entry', {
        'contributor': fields.String(required=True, description='contributor username'),
        'building_name': fields.String(required=True, description='building name'),
        'city_gml_file': fields.String(required=True, description='city gml file name'),
        'area_id': fields.Integer(required=True, description='area id')
    })
    verify = api.model('gml_verify', {
        'id': fields.Integer(required=True, description='id'),
        'validator': fields.String(required=True, description='validator username'),
        'status_id': fields.Integer(required=True, description='status id'),
        'reason': fields.String(required=False, description='reason')
    })
	
class CityGmlDto:
    api = Namespace('city_gml', description='city gml related operations')
    schema = api.model('city_gml', {
        'id': fields.Integer(dump_only=True),
        'contributor': fields.String(required=True, description='contributor username'),
        'city_gml_file': fields.String(required=True, description='city gml file name'),
        'uploaded_on': fields.DateTime(required=True, description='uploaded time'),
        'verified_on': fields.DateTime(required=True, description='verified time'),
        'validator': fields.String(required=True, description='validator username'),
        'reason': fields.String(required=True, description='reason'),
        'area' : fields.Nested(AreaDto().schema, required=True),
        'status' : fields.Nested(StatusDto().schema, required=True)
    })
    entry = api.model('city_gml_entry', {
        'contributor': fields.String(required=True, description='contributor username'),
        'city_gml_file': fields.String(required=True, description='city gml file name'),
        'area_id': fields.Integer(required=True, description='area id')
    })
    verify = api.model('city_gml_verify', {
        'id': fields.Integer(required=True, description='id'),
        'validator': fields.String(required=True, description='validator username'),
        'status_id': fields.Integer(required=True, description='status id'),
        'reason': fields.String(required=False, description='reason')
    })
	
class BuildingsDto:
    api = Namespace('buildings', description='buildings related operations')
    schema = api.model('buildings', {
        'id': fields.Integer(dump_only=True),
        'gml_id': fields.String(required=True, description='gml_id'),
        'city_gml' : fields.Nested(CityGmlDto().schema, required=True),
    })
    entry = api.model('buildings_entry', {
        'list_gml_id': fields.List(fields.String(required=True, description='gml id')),
        'city_gml_id': fields.Integer(required=True, description='city gml id')
    })
	
class MonitoringAttributeDto:
    api = Namespace('monitoring', description='monitoring attribute related operations')
    schema = api.model('monitoring_attribute', {
        'id': fields.Integer(dump_only=True),
        'timestamp': fields.DateTime(required=True, description='timestamp'),
        'name': fields.String(required=True, description='name'),
        'function': fields.String(required=True, description='function'),
        'height': fields.Float(required=True, description='height'),
        'buildings' : fields.Nested(BuildingsDto().schema, required=True),
		'contributor': fields.String(required=True, description='contributor username'),
        'verified_on': fields.DateTime(required=True, description='verified time'),
        'validator': fields.String(required=True, description='validator username'),
        'reason': fields.String(required=True, description='reason'),
        'status' : fields.Nested(StatusDto().schema, required=True)
    })
	
    entry = api.model('monitoring_attribute_entry', {
        'name': fields.String(required=True, description='name'),
        'function': fields.String(required=True, description='function'),
        'height': fields.Float(required=True, description='height'),
        'user_id' : fields.String(required=True, description='user public id'),
        'gml_id' : fields.String(required=True, description='building gml id')
    })
    verify = api.model('monitoring_attribute_verify', {
        'id': fields.Integer(required=True, description='id'),
        'validator': fields.String(required=True, description='validator username'),
        'status_id': fields.Integer(required=True, description='status id'),
        'reason': fields.String(required=False, description='reason')
    })

class MonitoringPhotoDto:
    api = Namespace('monitoring', description='monitoring photo related operations')
    schema = api.model('monitoring_photo', {
        'id': fields.Integer(dump_only=True),
        'timestamp': fields.DateTime(required=True, description='timestamp'),
        'photo_file': fields.String(required=True, description='photo_file'),
        'buildings' : fields.Nested(BuildingsDto().schema, required=True),
		'contributor': fields.String(required=True, description='contributor username'),
        'verified_on': fields.DateTime(required=True, description='verified time'),
        'validator': fields.String(required=True, description='validator username'),
        'reason': fields.String(required=True, description='reason'),
        'status' : fields.Nested(StatusDto().schema, required=True)
    })
    entry = api.model('monitoring_photo_entry', {
        'photo_file': fields.String(required=True, description='photo_file'),
        'user_id' : fields.String(required=True, description='user public id'),
        'gml_id' : fields.String(required=True, description='building gml id')
    })
    verify = api.model('monitoring_photo_verify', {
        'id': fields.Integer(required=True, description='id'),
        'validator': fields.String(required=True, description='validator username'),
        'status_id': fields.Integer(required=True, description='status id'),
        'reason': fields.String(required=False, description='reason')
    })


class MonitoringVideoDto:
    api = Namespace('monitoring', description='monitoring video related operations')
    schema = api.model('monitoring_video', {
        'id': fields.Integer(dump_only=True),
        'timestamp': fields.DateTime(required=True, description='timestamp'),
        'video_file': fields.String(required=True, description='video_file'),
        'buildings' : fields.Nested(BuildingsDto().schema, required=True),
		'contributor': fields.String(required=True, description='contributor username'),
        'verified_on': fields.DateTime(required=True, description='verified time'),
        'validator': fields.String(required=True, description='validator username'),
        'reason': fields.String(required=True, description='reason'),
        'status' : fields.Nested(StatusDto().schema, required=True)
    })
    entry = api.model('monitoring_video_entry', {
        'video_file': fields.String(required=True, description='video_file'),
        'user_id' : fields.String(required=True, description='user public id'),
        'gml_id' : fields.String(required=True, description='building gml id')
    })
    verify = api.model('monitoring_video_verify', {
        'id': fields.Integer(required=True, description='id'),
        'validator': fields.String(required=True, description='validator username'),
        'status_id': fields.Integer(required=True, description='status id'),
        'reason': fields.String(required=False, description='reason')
    })

class CityObjectDto:
    api = Namespace('cityobject', description='city object related operations')