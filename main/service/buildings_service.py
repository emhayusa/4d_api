import uuid
import datetime

from app.main import db
from app.main.model.buildings import Buildings

def save_new(data):
	for gml in data['list_gml_id']:
		print(gml)
		new = Buildings(
			gml_id=gml,
			city_gml_id=data['city_gml_id']
		)
		save_changes(new)
	response_object = {
		'status': 'success',
		'message': 'Successfully inserted.'
	}
	return response_object, 201
		
def get_all():
    return Buildings.query.order_by('id').all()

def get_by_id(id):
    return Buildings.query.filter_by(id=id).first()

def get_by_gml_id(gml_id):
    return Buildings.query.filter_by(gml_id=gml_id).first()
	
def save_changes(data):
    db.session.add(data)
    db.session.commit()