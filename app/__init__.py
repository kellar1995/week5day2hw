# from flask import Flask
# from config import Config
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager

# app = Flask(__name__)
# app.config.from_object(Config)

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
# login_manager.login_message = 'You are not allowed to access this page without being logged in.'
# login_manager.login_message_category = 'danger'


from flask import Flask, render_template
from config import Config
from .API.routes import api
from app.site.routes import site
from .authentication.routes import auth
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import db as root_db, login_manager, ma
from flask_cors import CORS
from helpers import JSONEncoder

app = Flask(__name__)
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'You are not allowed to access this page without being logged in.'
login_manager.login_message_category = 'danger'


app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

app.json_encoder = JSONEncoder
app.config.from_object(Config)
root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)