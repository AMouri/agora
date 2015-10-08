# Runs the api server
from agora_api import app
from agora_api.database.db import init_db

# init_db()
app.run(host='0.0.0.0')