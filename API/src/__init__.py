from flask import Flask
from config import config

#database
from database.Database import db

#routes

def init_app(configname):

    app = Flask(__name__)

    #Configuracion
    app.config.from_object(config[configname])

    #uso de orm
    db.init_app(app)

    #Blueprints

    return app
