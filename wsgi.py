import os

from app import create_app

flask_env = os.getenv("FLASK_ENV", "development")
application = create_app(flask_env)
