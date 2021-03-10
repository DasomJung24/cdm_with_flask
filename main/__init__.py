import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
cdm_dir = os.getcwd()
app.config.from_pyfile(f'{cdm_dir}/config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from .models.cdm import *
migrate = Migrate(app, db)

CORS(app)

from .controllers.cdm import person
# from .controllers.cdm.visit import visit_bp

app.register_blueprint(person.person_bp)
# app.register_blueprint(visit_bp)