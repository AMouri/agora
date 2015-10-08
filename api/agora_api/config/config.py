# Configuration file
import os

# Root location of the project
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

# Defines location of the DATABASE
DATABASE = os.path.join(PROJECT_ROOT, '../database', 'rooms.db')
# Turns on/off debug mode
DEBUG = True

#secret key. TODO: MAKE SECRET
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'