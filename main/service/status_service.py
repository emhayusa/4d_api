import uuid
import datetime

from app.main import db
from app.main.model.status import Status

def save_new(data):
	row = Status.query.filter_by(status_name=data['status_name']).first()
	if not row:
		new = Status(
			status_name=data['status_name'],
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
	        'message': 'Status already exists.',
		}
		return response_object, 409

def get_all():
    return Status.query.order_by('id').all()

def get_by_id(id):
    return Status.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()