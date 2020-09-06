from flask import request, jsonify
from flask_restplus import Resource
from ..config import CITYDB_CONNECTION_SERVER, CITYDB_CONNECTION_PORT, POSTGRES_DB_CITY, CITYDB_CONNECTION_USER, CITYDB_CONNECTION_PASSWORD
from ..util.dto import CityObjectDto
import psycopg2

api =  CityObjectDto.api


@api.route('/')
class CityObjectList(Resource):
	@api.doc('list_of_city_object')
	#@api.marshal_list_with(_schema, envelope='data')
	#@admin_token_required
	def get(self):
		"""List all City Object """
		# SQL to get records from Postgres
		db_conn = psycopg2.connect(host=CITYDB_CONNECTION_SERVER, port=CITYDB_CONNECTION_PORT, dbname=POSTGRES_DB_CITY, user=CITYDB_CONNECTION_USER, password=CITYDB_CONNECTION_PASSWORD)
		db_cursor = db_conn.cursor()
		s = "SELECT gmlid FROM cityobject"
		print(db_conn)
		print(db_cursor)
		print(s)
		# Error trapping
		try:
			# Execute the SQL
			db_cursor.execute(s)
			# Retrieve records from Postgres into a Python List
			list_objects = db_cursor.fetchall()
			#print(list_objects)
		except psycopg2.Error as e:
			t_message = "Database error: " + e + "/n SQL: " + s
			return ("error.html" + t_message)
		
		# Loop through the resulting list and print each object, along with a line break:
		#for i in range(len(list_objects)):
		#	print("CityObject " + str(list_objects[i]) + "\n")
		print(type(list_objects))
		list_dictionary = []
		#list_dictionary = { "gmlid" : a[0] for a in list_objects}
		
		for a in list_objects:
			#print(str(a))
			list_dictionary.append({"gmlid":a[0]})
			#print("gmlid: ", a[0])
		# Close the database cursor and connection
		db_cursor.close()
		db_conn.close()
		return jsonify(data=list_dictionary)
		#return get_all()
    #    return jsonify(get_paginated_list(
    #    get_all(), 
    #    '/', 
    #    start=request.args.get('start', 1), 
    #    limit=request.args.get('limit', 20)
    #))

@api.route('/last/<int:number>')
@api.param('number', 'The number row limit')
class CityObjectListLast(Resource):
	@api.doc('list_of_city_object_limit')
	#@api.marshal_list_with(_schema, envelope='data')
	#@admin_token_required
	def get(self, number):
		"""List all City Object limit by number"""
		# SQL to get records from Postgres
		db_conn = psycopg2.connect(host=CITYDB_CONNECTION_SERVER, port=CITYDB_CONNECTION_PORT, dbname=POSTGRES_DB_CITY, user=CITYDB_CONNECTION_USER, password=CITYDB_CONNECTION_PASSWORD)
		db_cursor = db_conn.cursor()
		s = "SELECT gmlid FROM cityobject order by id desc limit " + str(number)
		print(db_conn)
		print(db_cursor)
		print(s)
		# Error trapping
		try:
			# Execute the SQL
			db_cursor.execute(s)
			# Retrieve records from Postgres into a Python List
			list_objects = db_cursor.fetchall()
			#print(list_objects)
		except psycopg2.Error as e:
			t_message = "Database error: " + e + "/n SQL: " + s
			return ("error.html" + t_message)
		
		# Loop through the resulting list and print each object, along with a line break:
		#for i in range(len(list_objects)):
		#	print("CityObject " + str(list_objects[i]) + "\n")
		print(type(list_objects))
		list_dictionary = []
		#list_dictionary = { "gmlid" : a[0] for a in list_objects}
		
		for a in list_objects:
			#print(str(a))
			list_dictionary.append({"gmlid":a[0]})
			#print("gmlid: ", a[0])
		# Close the database cursor and connection
		db_cursor.close()
		db_conn.close()
		return jsonify(data=list_dictionary)