from agora_api import app
from agora_api.database.db import init_db
from flask import g
import os
import tempfile
import unittest

class RoutesRoomCreateTestCase(unittest.TestCase):

	def setUp(self):
		self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
		app.config['TESTING'] = True
		self.app = app.test_client()
		init_db()

	def tearDown(self):
		os.close(self.db_fd)
		os.unlink(app.config['DATABASE'])

	def test_room_create(self):
		"""
		Tests that the /room/create route creates a room with a unique id
		"""
		response_one = self.room_create().data
		assert int(response_one) == 1
		response_two = self.room_create().data
		assert int(response_two) == 2

	def room_create(self):
		"""
		Wrapper for creating a room
		"""
		return self.app.put('/room/create')


if __name__ == '__main__':
	unittest.main()