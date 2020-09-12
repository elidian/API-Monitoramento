# coding: utf-8
# instacia do app Flask

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from api import models
from api.controllers import user_controller, cam_controller, default_controller