import uuid
import datetime

from app.main import db
from app.main.model.area import Area

def save_new(data):
	row = Area.query.filter_by(area_name=data['area_name']).first()
	if not row:
		new = Area(
			area_name=data['area_name'],
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
	        'message': 'Area already exists.',
		}
		return response_object, 409

def get_all():
    return Area.query.order_by('id').all()

def get_by_id(id):
    return Area.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()