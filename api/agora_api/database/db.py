import sqlite3

from agora_api import app
from contextlib import closing
from flask import g

@app.before_request
def before_request():
	g.db = connect_db()

def connect_db():
	"""
	Connects to the database
	"""
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
	"""
	Initializes our database
	"""
	with closing(connect_db()) as db:
		with app.open_resource('database/schemas/room.sql', mode = 'r') as f:
			db.cursor().executescript(f.read())
		db.commit()

@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()
