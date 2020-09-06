import uuid
import datetime

from app.main import db
from app.main.model.citygml import CityGml

def save_new(data):
	new = CityGml(
		contributor=data['contributor'],
		city_gml_file=data['city_gml_file'],
		area_id=data['area_id'],
		uploaded_on=datetime.datetime.utcnow(),
		status_id=1			
	)
	save_changes(new)
	response_object = {
		'status': 'success',
		'message': 'Successfully inserted.'
	}
	return response_object, 201

def verify(data):
	row = CityGml.query.filter_by(id=data['id']).first()
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
			
def get_all():
    return CityGml.query.order_by('id').all()

def get_by_id(id):
    return CityGml.query.filter_by(id=id).first()

def get_by_username(username):
    return CityGml.query.filter_by(contributor=username).order_by('uploaded_on').all()

def get_by_area(id):
    return CityGml.query.filter_by(area_id=id).order_by('uploaded_on').all()
	
def save_changes(data):
    db.session.add(data)
    db.session.commit()