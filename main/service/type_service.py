import uuid
import datetime

from app.main import db
from app.main.model.type import Type

def save_new(data):
	row = Type.query.filter_by(type_name=data['type_name']).first()
	if not row:
		new = Type(
			type_name=data['type_name'],
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
	        'message': 'Type already exists.',
		}
		return response_object, 409

def get_all():
    return Type.query.order_by('id').all()

def get_by_id(id):
    return Type.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()