from agora_api import app
from flask import flash, g

@app.route('/')
def hello_world():
	"""
	Temporary index page as boilerplate
	"""
	return 'Hello World!'

@app.route('/room/create', methods=['PUT'])
def room_create():
	"""
	Creates a room in the rooms database. Returns the id of the room.
	"""
	g.db.execute('insert into rooms VALUES(null)')
	room_id = g.db.execute('select last_insert_rowid()').fetchone()[0]
	g.db.commit()
	flash('New room successfully created')
	return str(room_id)