import uuid
import datetime

from app.main import db
from app.main.model.monitoring_photo import MonitoringPhoto
from app.main.model.user import User
from app.main.model.buildings import Buildings
from app.main.model.citygml import CityGml

def save_new_photo(data):
	row = User.query.filter_by(public_id=data['user_id']).first()
	if row:
		building = Buildings.query.filter_by(gml_id=data['gml_id']).first()
		if building:
			print(data)
			new = MonitoringPhoto(
				timestamp=datetime.datetime.utcnow(),
				photo_file=data['photo_file'],
				contributor=row.username,
				buildings_id=building.id,
				status_id=1
			)
			save_changes(new)
			response_object = {
				'status': 'success',
				'message': 'Successfully inserted.'
			}
			return response_object, 201
		else:
			response_object = {
			'status': 'fail',
			'message': 'GML ID is not found.',
			}
			return response_object, 404
	else:
		response_object = {
			'status': 'fail',
			'message': 'User ID is not found.',
		}
		return response_object, 404

def verify_photo(data):
	row = MonitoringPhoto.query.filter_by(id=data['id']).first()
	if row:
		setattr(row, 'validator', data['validator'])
		setattr(row, 'verified_on', datetime.datetime.utcnow())
		setattr(row, 'status_id', data['status_id']) # ACTIVATED
		setattr(row, 'reason', data['reason'])
		db.session.commit()
		response_object = {
			'status': 'success',
			'message': 'Successfully verified',
		}
		return response_object, 202
		#send email activated
		#return send_email_activation(row)
		#return send_to_old_system(row,  data['password'])
	else:
		response_object = {
			'status': 'fail',
			'message': 'City Gml  ID is not found.',
		}
		return response_object, 404
		
def get_all_photo():
    return MonitoringPhoto.query.order_by('timestamp').all()

def get_all_count_photo():
    return MonitoringPhoto.query.count()

def get_by_id_photo(id):
    return MonitoringPhoto.query.filter_by(id=id).first()

def get_by_user_id_photo(user_id):
	row = User.query.filter_by(public_id=user_id).first()
	if row:
		return MonitoringPhoto.query.filter_by(contributor=row.username).order_by(MonitoringPhoto.timestamp.desc()).all()
	else:
		response_object = {
			'status': 'fail',
			'message': 'User ID is not found.',
		}
		return response_object, 404
	
def get_by_gml_id_photo(id):
	row = Buildings.query.filter_by(gml_id=id).first()
	if row:
		return MonitoringPhoto.query.filter_by(buildings_id=row.id, status_id=3).order_by(MonitoringPhoto.timestamp.desc()).all()
	else:
		response_object = {
			'status': 'fail',
			'message': 'GML ID is not found.',
		}
		return response_object, 404

def get_by_gml_id_last_photo(id):
	row = Buildings.query.filter_by(gml_id=id).first()
	if row:
		return MonitoringPhoto.query.filter_by(buildings_id=row.id, status_id=3).order_by(MonitoringPhoto.timestamp.desc()).first()
	else:
		return None


def get_by_area_photo(id):
	#rows = MonitoringAttribute.query.join(CityGml.id).join(Buildings.id).filter(CityGml.id==id).order_by(MonitoringAttribute.timestamp.desc()).all()
	#filter_by(area_id=id).order_by('uploaded_on').all()
	#rows = MonitoringAttribute.query.filter_by(buildings_id=id).from_self().join(CityGml.building_id).all()
	#rows = MonitoringAttribute.query.join(Buildings).join(CityGml).filter(CityGml.id==id).order_by(MonitoringAttribute.timestamp.desc()).all()
	return  MonitoringPhoto.query.join(Buildings).join(CityGml).filter(CityGml.id==id).order_by(MonitoringPhoto.timestamp.desc()).all()
	
def save_changes(data):
    db.session.add(data)
    db.session.commit()